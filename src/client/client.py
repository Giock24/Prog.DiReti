import os
import subprocess
import sys
import time
import socket as sk

# this method return a list of all file that are present on client folder
def listingFiles():
    lista = os.listdir(os.path.join(os.getcwd(), "myFiles"))
    return lista

def itsOK(string):
    if string[9:12] == "200":
        print("The operation had succeed")

commands=['ls','upload','download','exit']
serverFiles=[]

print('Creation of all files')

pathabs = os.getcwd();
#print(pathabs[0:-7])

pathScript = ""+pathabs[0:-6]+"removeAllFiles.sh"
subprocess.call([pathScript])
pathScript = ""+pathabs[0:-6]+"createFiles.sh"
subprocess.call([pathScript])

clientSocket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)

server_address = ('localhost', 10000)

while True:
    
    print('Commands available : %s' % (commands.__str__()))
    command = input("Digit a command : ")
    
    if commands.__contains__(command) and command != "exit":
    
        try:
            
            if command == "ls":
                serverFiles.clear()
                sent = clientSocket.sendto(command.__str__().encode('utf8'), server_address)
            
                print('Waiting to receive from')
                data, server = clientSocket.recvfrom(4096)
                
                length = int(data.decode('utf8'))
                
                for i in range(length):
                    data = clientSocket.recv(4096)
                    serverFiles.append(data.decode('utf8'))
                
                time.sleep(2)
                
                print('Waiting for OK')
                data = clientSocket.recv(4096)
                responseServer = data.decode('utf8')
                
                itsOK(responseServer)
                
                print('Files that are present in the Server: %s \n' % (serverFiles.__str__()) )
                
            elif command == "upload":
                fileToUpload=""
                
                while True:
                    lista = listingFiles()
                    
                    print('You have these files : %s' % lista.__str__())
                    fileToUpload = input("Digit a file to upload : ")
                    
                    if lista.__contains__(fileToUpload):
                        break
                    else:
                        print("This file doesn't exists! Try Again")
                        
                sent = clientSocket.sendto(command.__str__().encode('utf8'), server_address)
                
                time.sleep(2)
                print('Waiting for OK')
                
                data, server = clientSocket.recvfrom(4096)
                responseServer = data.decode('utf8')
                
                itsOK(responseServer)
                
                sent = clientSocket.sendto(fileToUpload.__str__().encode('utf8'), server_address)
                
                pathFolder = os.path.join(os.getcwd(), "myFiles")
                pathFolder = os.path.join(pathFolder, ""+fileToUpload+"")
                
                file = open(""+pathFolder+"",'r')
                
                sent = clientSocket.sendto(file.read().__str__().encode('utf8'), server_address)
                
                file.close()
                
                print('Waiting Ending of Upload')
                data = clientSocket.recv(4096)
                
                responseServer = data.decode('utf8')
                itsOK(responseServer)
        
        except Exception as Info:
            print(Info)
            #print("Something gone wrong")
    
    elif command == "exit":
        print("\n\r Exit with success")
        
        pathScript = ""+pathabs[0:-6]+"removeAllFiles.sh"
        subprocess.call([pathScript])
        
        clientSocket.close()
        sys.exit()
    else:
        print("Invalid command try Again!\n")
    
    # connectionSocket, addr = clientSocket.connect('127.0.0.1')
    
    


