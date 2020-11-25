import socket

s = socket.socket()

port = 8888

s.connect(('192.168.0.103', port))

data, addr = s.recvfrom(1024)

s.sendto(b'Hi, saya client. Terima Kasih!', ('192.168.0.103', port))
print(data)

s.close()

