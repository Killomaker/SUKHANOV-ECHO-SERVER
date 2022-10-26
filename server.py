import pickle
import socket 

print('Server launched')

sock = socket.socket()
sock.bind(('', 9090))

print('Starting. . .')
sock.listen(1)

print('Connecting. . .')

connec, adr = sock.accept()

print('Getting data. . .')

mes = connec.recv(1024).decode()
print(mes)


print('Sending. . .')
connec.send(mes.encode())

print('Turning off the client')
connec.close()

print('Server turned off')
