import os
import subprocess
import sys
import socket as sk

print('Creation of all files')

pathabs = os.getcwd();
#print(pathabs[0:-7])

pathScript = ""+pathabs[0:-6]+"createFiles.sh"
subprocess.call([pathScript])

clientSocket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)

server_address = ('localhost', 10000)
clientSocket.bind(server_address)

while True:
    
    print("Commands available : 'ls', 'upload', 'download', 'Exit'\n")
    command = input("Digit a command : ")
    
    if command == "ls" or command == "upload" or command == "download":
    
        try:
            print("sa")
        
        except:
            print("Something gone wrong")
        finally:
            clientSocket.close()
    
    elif command == "Exit":
        print("\n\r Exit with success")
        
        clientSocket.close()
        sys.exit()
    else:
        print("\n Invalid command try Again!")
    
    # connectionSocket, addr = clientSocket.connect('127.0.0.1')
    
    


