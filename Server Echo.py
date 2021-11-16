import socket
s = socket.socket()
print('Socket Created')
s.bind(('localhost',9999))
s.listen(3)
# print('Waiting for connections')
c, addr = s.accept()
while(True):
    data = c.recv(2048)
    if data:
     print("Received from client: %s" % data)
    c.send(data)
c.close()