import os
import sys
import socket as sk

# this method return a list of all file that are present on Server
def listingFiles():
    lista = os.listdir(os.path.join(os.getcwd(), "serverStorage"))
    return lista

serverPort = 10000
serverSocket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM);

# nel primo paramentro di entrata presumo come IP : 127.0.0.1
serverSocket.bind('',serverPort)

print('The server is Online on port: ', serverPort)

while True:
    
    print("\n\r waiting to receive message...")
    
    # data = dato ricevuto dal client
    # addr = indirizzo del client
    data, addr = serverSocket.recvfrom(4096)
    
    print('\n\r received %s bytes from %s' % (len(data), addr))
    print(data.decode('utf8'))
    
    try:
        
        if len(data)>0:
            
            
            
            if data == "ls":
                lista = listingFiles()
                for file in lista:
                    sent = serverSocket.sendto(file.encode('utf8'), addr)
                
                responseServer='HTTP/1.1 200 OK List_Files_Sended'
                sent = serverSocket.sendto(responseServer.encode(), addr)
                print('\n\r sended this list %s' % lista.__str__())
            else:
                print("\n\r Command Not Found")
            
        else:
            print("\n\r The message received is empty")
        
    except:
        print("\n\r Something gone wrong")
    
    
serverSocket.close()
sys.exit()
    
    
    
