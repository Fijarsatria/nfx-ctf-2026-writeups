"""GF(2^128) GCM helpers + forbidden-attack H recovery via linear monomial solve."""
from Crypto.Cipher import AES
import os

MASK=(1<<128)-1
def gf_mul(x,y):
    z=0; v=x & MASK
    for i in range(128):
        if (y>>(127-i))&1: z^=v
        if v&1: v=(v>>1)^(0xE1<<120)
        else: v>>=1
    return z & MASK
def gf_pow(a,e):
    r=1<<127  # multiplicative identity in GCM integer convention
    while e:
        if e&1: r=gf_mul(r,a)
        a=gf_mul(a,a); e>>=1
    return r
def gf_inv(a):
    assert a!=0
    return gf_pow(a,(1<<128)-2)
def gf_div(a,b): return gf_mul(a,gf_inv(b))

def blocks16(data):
    out=[]
    for i in range(0,len(data),16):
        out.append(int.from_bytes(data[i:i+16].ljust(16,b'\0'),'big'))
    return out
def ghash(h,ct,aad=b''):
    y=0
    for b in blocks16(aad): y=gf_mul(y^b,h)
    for b in blocks16(ct): y=gf_mul(y^b,h)
    L=((len(aad)*8)<<64)|(len(ct)*8)
    y=gf_mul(y^L,h)
    return y
def ekj0(key,nonce):
    return int.from_bytes(AES.new(key,AES.MODE_ECB).encrypt(nonce+b'\0\0\0\1'),'big')
def hkey(key):
    return int.from_bytes(AES.new(key,AES.MODE_ECB).encrypt(b'\0'*16),'big')
def tag_of(key,nonce,ct,aad=b''):
    return ghash(hkey(key),ct,aad)^ekj0(key,nonce)

def nullspace(A,ncols):
    A=[row[:] for row in A]
    piv=[]; r=0
    for c in range(ncols):
        p=None
        for i in range(r,len(A)):
            if A[i][c]!=0: p=i;break
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        inv=gf_inv(A[r][c])
        A[r]=[gf_mul(v,inv) for v in A[r]]
        for i in range(len(A)):
            if i!=r and A[i][c]!=0:
                f=A[i][c]
                A[i]=[A[i][j]^gf_mul(f,A[r][j]) for j in range(ncols)]
        piv.append(c); r+=1
        if r==len(A): break
    free=[c for c in range(ncols) if c not in piv]
    basis=[]
    for fc in free:
        x=[0]*ncols; x[fc]=1<<127  # 1 in field
        for ri,pc in enumerate(piv):
            x[pc]=A[ri][fc]
        basis.append(x)
    return basis
def recover_H_from_pairs(pairs, nblocks):
    # pairs: list of (ct_bytes, tag_int); same length, no AAD
    cols=nblocks  # exponents 2..nblocks+1
    A=[]
    for (c1,t1),(c2,t2) in zip(pairs,pairs[1:]):
        b1=blocks16(c1); b2=blocks16(c2)
        # n data blocks exactly
        row=[0]*cols
        for i in range(1,nblocks+1):
            e=nblocks-i+2  # exponent
            col=e-2
            row[col]=b1[i-1]^b2[i-1]
        A.append(row)
    basis=nullspace(A,cols)
    for x in basis:
        if x[0]==0: continue
        H=gf_div(x[1],x[0])
        # consistency: x[e] should equal H^e (up to scale) -> check ratios
        ok=True
        cur=x[1]
        for k in range(2,cols+1):
            if x[k-1]!=cur: ok=False;break
            cur=gf_mul(cur,H)
        if ok:
            return H
    return None

def solve_linear(A,b,ncols):
    """Return (particular solution with free vars 0, pivot cols, rank) or None if inconsistent."""
    M=[row[:]+[bb] for row,bb in zip(A,b)]
    m=len(M); r=0; piv=[]
    for c in range(ncols):
        p=None
        for i in range(r,m):
            if M[i][c]!=0: p=i;break
        if p is None: continue
        M[r],M[p]=M[p],M[r]
        inv=gf_inv(M[r][c])
        M[r]=[gf_mul(v,inv) for v in M[r]]
        for i in range(m):
            if i!=r and M[i][c]!=0:
                f=M[i][c]
                M[i]=[M[i][j]^gf_mul(f,M[r][j]) for j in range(ncols+1)]
        piv.append(c); r+=1
        if r==m: break
    for i in range(r,m):
        if all(M[i][c]==0 for c in range(ncols)) and M[i][ncols]!=0:
            return None
    x=[0]*ncols
    for i,c in enumerate(piv):
        x[c]=M[i][ncols]
    return x,piv,r

def recover_H_general(pairs, nblocks):
    """pairs: (ct_bytes, tag_int), all same length. Solve linear system in H^2..H^(n+1)."""
    n=len(pairs)
    eqs=[]
    for i in range(n):
        for j in range(i+1,n):
            c1,t1=pairs[i]; c2,t2=pairs[j]
            b1=blocks16(c1); b2=blocks16(c2)
            coeff={}
            for k in range(1,nblocks+1):
                e=nblocks-k+2
                d=b1[k-1]^b2[k-1]
                if d: coeff[e]=coeff.get(e,0)^d
            if coeff:
                eqs.append((coeff,t1^t2))
    exps=sorted({e for coeff,_ in eqs for e in coeff})
    if not exps: return None
    A=[];b=[]
    for coeff,rhs in eqs:
        A.append([coeff.get(e,0) for e in exps]); b.append(rhs)
    sol=solve_linear(A,b,len(exps))
    if sol is None: return None
    x,pivs,rank=sol
    # derive H from consecutive exponents whose variables are pivot (determined)
    cands=set()
    for i in range(len(exps)-1):
        if exps[i+1]==exps[i]+1 and x[i]!=0 and x[i+1]!=0:
            cands.add(gf_div(x[i+1],x[i]))
    for H in cands:
        E=set()
        ok=True
        for ct,t in pairs:
            E.add(t^ghash(H,ct))
            if len(E)>1: ok=False;break
        if ok and len(E)==1:
            return H
    return None
