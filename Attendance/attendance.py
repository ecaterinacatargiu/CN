import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.connect(("172.30.112.77", 8888))
s.send(b"Catargiu Georgiana Ecaterina")

s.close()