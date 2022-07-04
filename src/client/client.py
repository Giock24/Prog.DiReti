import os
import subprocess

from socket import *

print('Creation of all files')

pathabs = os.getcwd();
#print(pathabs[0:-7])

pathScript = ""+pathabs[0:-6]+"createFiles.sh"
subprocess.call([pathScript])

clientPort = 85

clientSocket = socket(AF_INET, SOCK_DGRAM)

clientSocket.bind('',serverPort)


