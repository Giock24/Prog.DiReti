import os

from socket import *

serverPort = 8080

serverSocket = socket(AF_INET, SOCK_DGRAM);

# nel primo paramentro di entrata presumo come IP : 127.0.0.1
serverSocket.bind('',serverPort)

serverSocket.listen(1)

print('The server is Online on port: ', serverPort)

while true:
    # nella var connectioSocket viene messo un oggetto
    # per poter comunicare con il client
    
    # addr = indirizzo del client
    connectionSocket, addr = serverSocket.accept()
    
    try:
        
        message = connectionSocket.recv(4096)
        
        if len(message.split())>0:
            print("")
        else:
            print("The request is empty")
        
    except:
        print("Something gone wrong")
    
    
    
    
    
    
