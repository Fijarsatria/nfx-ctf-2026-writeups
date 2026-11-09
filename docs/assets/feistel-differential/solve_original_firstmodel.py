from z3 import *
from cipher import encrypt_block,key_schedule,decrypt_block
SBOX=[1,8,14,12,2,0,3,4,11,9,15,13,6,10,7,5]
def sl(n):
    e=BitVecVal(SBOX[15],4)
    for i in range(14,-1,-1): e=If(n==BitVecVal(i,4),BitVecVal(SBOX[i],4),e)
    return e
def F(x,k):
    y=x^k
    m=Concat(sl(Extract(15,12,y)),sl(Extract(11,8,y)),sl(Extract(7,4,y)),sl(Extract(3,0,y)))
    return Concat(Extract(11,8,m),Extract(15,12,m),Extract(3,0,m),Extract(7,4,m))
def enc(block,ks):
    L=Extract(31,16,block);R=Extract(15,0,block)
    for k in ks: L,R=R,L^F(R,k)
    return Concat(L,R)
blocks=[]; cur=None; diff=0
for line in open('pairs.txt'):
    line=line.strip()
    if not line: continue
    if line.startswith('#'):
        diff=int(line.split(':')[-1].strip(),16); cur=[]; blocks.append((diff,cur)); continue
    a,b,c=line.split(); cur.append((int(a,16),int(b,16),int(c,16)))
print('blocks',[(hex(d),len(l)) for d,l in blocks], 'total',sum(len(l) for d,l in blocks))
def solve(sel,diff):
    ks=[BitVec(f'k{i}',16) for i in range(7)]
    s=Solver(); s.set(timeout=120000)
    for p,c1,c2 in sel:
        s.add(enc(BitVecVal(p,32),ks)==BitVecVal(c1,32))
        s.add(enc(BitVecVal(p,32)^BitVecVal(diff,32),ks)==BitVecVal(c2,32))
    assert s.check()==sat
    m=s.model(); sv=[m.eval(k).as_long() for k in ks]
    return key_schedule(sum(sv[i]<<(16*i) for i in range(7)))
d0,blk0=blocks[0]
ks=solve(blk0[:6],d0)
print('recovered full key:',[hex(x) for x in ks])
master=sum(ks[i]<<(16*i) for i in range(7))
print('master',hex(master))
tot=0;ok=0;bad=0
for diff,lst in blocks:
    for p,c1,c2 in lst:
        tot+=1
        if encrypt_block(p,ks)==c1 and encrypt_block(p^diff,ks)==c2: ok+=1
        else:
            bad+=1
            if bad<=3: print('BAD diff',hex(diff),hex(p))
print('verify total',tot,'ok',ok,'bad',bad)
ct=bytes.fromhex(open('flag.enc').read().strip())
pt=b''
for i in range(0,len(ct),4):
    pt+=decrypt_block(int.from_bytes(ct[i:i+4],'big'),ks).to_bytes(4,'big')
print('FLAGPT',repr(pt))
