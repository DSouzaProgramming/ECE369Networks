import socket


serverPort = 134
serverSocket = socket(socket.AF_INET,socket.SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print('Bonesaw is readyyyy')

while 1:
    message, clientAddr = serverSocket.recvfrom(1024)
    modifiedMessage = message.upper()
    serverSocket.sendto(modifiedMessage,clientAddr)
