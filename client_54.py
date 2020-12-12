import socket
import sys
#import json
import re

file = open('file.txt', 'r')
file1 = file.read()
#print(file1)
#filename = str(file1.encode)
#sendData = json.dumps(file1)

s = socket.socket()

port = 8080
s.connect(('192.168.0.103', port))
'''
print("Which file you want to sent?")
filename = input("Enter filename:")
print("Filename: " + filename)

check = re.search(filename, file1)

if check:
	s.send(str.encode(filename))
else:
	message = "Error"
	s.send(str.encode(message))
'''
#while True:
s.send(str.encode(file1))
#data = s.recv(4096)
#print(data)


#s.send(str.encode(file1))
#file1 = file.read()
#file.close()
print("Done sending")

#s.send(file1)
#s.sendall(bytes(sendData,encoding="utf-8"))

s.close()



