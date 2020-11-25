import socket

ClientSocket = socket.socket()
<<<<<<< HEAD
host = '192.168.0.103'
=======
host = '192.168.114.6'
>>>>>>> f886aea5d1851ba58214e2c5da0fb681516734a4
port = 8889

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)
print(Response)
while True:
    Input = input('Say Something: ')
    ClientSocket.send(str.encode(Input))
    Response = ClientSocket.recv(1024)
<<<<<<< HEAD
    #print(Response.decode('utf-8'))
=======
    print(Response.decode('utf-8'))
>>>>>>> f886aea5d1851ba58214e2c5da0fb681516734a4

ClientSocket.close()

