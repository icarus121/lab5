import socket
import sys
import os
from _thread import *

s = socket.socket()
print("Socket Created")

host = ''
port = 8080

ThreadCount = 0
try:
    s.bind((host, port))
except socket.error as e:
    print(str(e))


#s.bind(('', port))
print("Socket binded to: " + str(port))

s.listen(5)
print("Socket is listening")

def threaded_c(connection):
    connection.send(str.encode('Welcome to the Server\n'))
    while True:
        data = connection.recv(4096)
        reply = 'Server Says: ' + data.decode('utf-8')
        if not data:
            break
        connection.sendall(str.encode(reply))
    connection.close()


while True:
	c, addr = s.accept()
	print("Connected to: " + addr[0] + ':' + str(addr[1]))
	start_new_thread(threaded_c, (c, ))
	ThreadCount+=1
	print('Thread Number: ' + str(ThreadCount))

	data = c.recv(4096)
	data = data.decode("utf 8")
	print(data)

s.close()
