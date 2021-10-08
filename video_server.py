import socket
import cv2
import pickle
import struct
import imutils

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_name = socket.gethostname()
host_ip = '127.0.0.1'
print('HOST IP: ',host_ip)
port = 12000
socket_address = (host_ip,port)
print('socket created')

server_socket.bind(socket_address)
print('socket bind completed')

server_socket.listen(7)
print('socket is now listening')

while True:
    client_socket,addr = server_socket.accept()
    print('connection from : ',addr)
    if client_socket:
        vid = cv2.VideoCapture(0)
        while(vid.isOpened()):
            img,frame = vid.read()
            a = pickle.dumps(frame)
            message = struct.pack("Q",len(a))+a
            client_socket.sendall(message)
            cv2.imshow('sending...',frame)
            key = cv2.waitKey(10)
            if key ==13:
                client_socket.close()