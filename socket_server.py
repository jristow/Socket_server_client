import socket

s = socket.socket()

print("Socket successfully created")

port = 9500

s.bind(('',port))

print("socket binded to %s" %(port))

s.listen(5)

print('socket is listening')


while True:

    c, addr = s.accept()
    print('Got connection from' + str(addr))
    message = (c.recv(1024))
    print(message.decode())
    if message == bytes('Hello', 'utf-8'):
        c.send(bytes('Hi','utf-8'))
        c.close()
    else:
        c.send(bytes('Goodbye', 'utf-8'))
        c.close()
  
    