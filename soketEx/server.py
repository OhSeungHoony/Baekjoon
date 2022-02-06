import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(("", 9999))
serversocket.listen(1)

(sock, addr) = serversocket.accept()

sock.send(b"Hello, Client.")

str = sock.recv(100)
print(str)

sock.close()
serversocket.close()