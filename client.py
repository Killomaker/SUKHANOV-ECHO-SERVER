import pickle
import socket

sock = socket.socket()
print('Connecting. . .')
sock.connect(('localhost', 9090))

print("Sending data to server")

mess = str(input('Input message: '))
sock.send(mess.encode())


print('Getting data from server. . .')
print(sock.recv(1024).decode())

print('Disconnecting. . .')
sock.close()
