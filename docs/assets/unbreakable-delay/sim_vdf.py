#!/usr/bin/env python3
"""[SIMULASI] VDF bypass via XOR-structured modulus + Euler phi.

The original NFX/UnbreakableDelay service is no longer reachable and no
source/instance was bundled.  This script demonstrates the attack family
named by the verified flag: factor N because the two primes differ by a
single XOR bit, then reduce the 2^256 sequential exponent modulo phi(N)
and forge the Fiat-Shamir proof.

NOT the original challenge output -- labelled SIMULASI in the writeup.
"""
import hashlib
from sympy import nextprime, isprime

BITS = 512
XOR_BIT = 300

# --- build a toy instance with an XOR relation p ^ q = 2^XOR_BIT ---
p = nextprime((1 << (BITS - 1)) | 0x5EEDBEEF123456789)
while True:
    q = p ^ (1 << XOR_BIT)
    if isprime(q):
        break
    p = nextprime(p + 1)
assert isprime(p) and isprime(q)
N = p * q
print("[instance] N bits       =", N.bit_length())
print("[instance] p ^ q        =", hex(p ^ q))
print("[instance] p            =", hex(p))

# --- attack step 1: XOR factoring ---
# p ^ q = 2^k  =>  |q-p| = 2^k ; try both signs.
found = None
for sign in (+1, -1):
    delta = sign * (1 << XOR_BIT)
    # p(p+delta)=N  ->  p = (-delta + sqrt(delta^2+4N))/2
    D = delta * delta + 4 * N
    import math
    r = math.isqrt(D)
    for cand in (r - 1, r, r + 1):
        if cand * cand == D:
            pp = (-delta + cand) // 2
            if pp > 1 and N % pp == 0:
                found = (pp, N // pp)
                break
    if found:
        break
assert found
p2, q2 = found
print("[attack]  factored N    =", p2 * q2 == N, " p == p2:", p2 == p)

# --- attack step 2: fast VDF evaluation using phi ---
phi = (p2 - 1) * (q2 - 1)
x = 2
T = 1 << 256                      # the "trillion years" sequential exponent
e = pow(2, 256, phi)              # 2^T mod phi
y = pow(x, e, N)                  # == x^(2^256) mod N
print("[attack]  y = 2^(2^256) mod N computed instantly with the phi shortcut")

# --- attack step 3: forge the Fiat-Shamir proof ---
def H(*parts):
    h = hashlib.sha256()
    for a in parts:
        h.update(int(a).to_bytes((int(a).bit_length() + 7) // 8 or 1, "big"))
    return int.from_bytes(h.digest(), "big")

l = int(nextprime(H(x, y) % (1 << 64)))    # challenge prime
pi = pow(x, (T // l) % phi, N)             # proof, fast because we know phi
lhs = (pow(pi, l, N) * pow(x, T % l, N)) % N
print("[attack]  challenge l    =", hex(l))
print("[attack]  proof pi       =", hex(pi)[:48], "...")
print("[verify]  pi^l * x^(T%l) == y mod N :", lhs == y)
