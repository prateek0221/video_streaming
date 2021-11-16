import socket
c = socket.socket()
try:
    c.connect(('localhost',9999))
    msg = input("client> ")
    while msg != 'exit':
        c.sendall(msg.encode('utf-8'))
        data = c.recv(2048)
        print("Received : %s" % data.decode('utf-8'))
        msg = input('client> ')
except socket.gaierror as e:
    print("Socket error:%s" % str(e))
except Exception as e:
    print(e)
finally:
    c.close()

