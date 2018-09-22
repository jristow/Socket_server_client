import socket

s = socket.socket()

port = 9500

s.connect(('127.0.0.1', port))
s.send(bytes('Hello', 'utf-8'))
response = s.recv(1024)
print(response.decode())
s.close 
