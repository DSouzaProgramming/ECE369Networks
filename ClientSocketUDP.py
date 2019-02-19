import socket

serverName = '127.0.0.1'
serverPort = 134

clientSocket = socket(socket.AF_INET,socket.SOCK_DGRAM)
message = input('Input lowercase sentence:\n')
clientSocket.sendto(message, (serverName,serverPort))

modifiedMessage, serverAddress = clientSocket.recvfrom(1024)

print(modifiedMessage)

clientSocket.close()

