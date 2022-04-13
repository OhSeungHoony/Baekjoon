import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(("192.168.0.25", 9999))

clientsocket.send(b"Hello, Server")

str = clientsocket.recv(100)
print(str)

clientsocket.close()