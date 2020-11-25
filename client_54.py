import socket
import sys
import json

file = open('file.txt', 'r')
file1 = file.read()
print(file1)
sendData = json.dumps(file1)

s = socket.socket()

port = 8080
s.connect(('192.168.0.103', port))

s.sendall(bytes(sendData,encoding="utf-8"))

s.close()



