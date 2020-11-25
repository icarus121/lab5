import socket

s = socket.socket()

port = 8889

s.connect(('192.168.0.103', port))

data = s.recv(1024)
print(data)
s.send(b'Hi, saya client. Terima Kasih!')
#print(data)
s.close()

