import os
import sys
import socket as sk

# this method return a list of all file that are present on Server
def listingFiles():
    lista = os.listdir(os.path.join(os.getcwd(), "serverStorage"))
    return lista

#serverPort = 10000
serverSocket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM);

# nel primo paramentro di entrata presumo come IP : 127.0.0.1
server_address = ('localhost', 10000)
serverSocket.bind(server_address)

print('The server is Online on %s port: %s' % server_address)

while True:
    
    print("\n\r waiting to receive message...")
    
    # data = dato ricevuto dal client
    # addr = indirizzo del client
    data, addr = serverSocket.recvfrom(4096)
    
    print('\n\r received %s bytes from %s' % (len(data), addr))
    command = data.decode('utf8')
    print(command)
    
    try:
        
        if len(command)>0:
            
            
            
            if command == "ls":
                lista = listingFiles()
                
                sent = serverSocket.sendto(len(lista).__str__().encode('utf8'), addr)
                
                for file in lista:
                    sent = serverSocket.sendto(file.encode('utf8'), addr)
                
                responseServer='HTTP/1.1 200 OK List_Files_Sended'
                sent = serverSocket.sendto(responseServer.encode(), addr)
                print('\n\r sended this list %s' % lista.__str__())
                
            elif command == "upload":
                
                responseServer='HTTP/1.1 200 OK Ready_To_Receive_File'
                
                sent = serverSocket.sendto(responseServer.encode(), addr)
                
                print("Waiting the uploading of file...")
                data = serverSocket.recv(4096)
                fileToUpload = data.decode('utf8')
                
                pathFolder = os.path.join(os.getcwd(),"serverStorage")
                pathFolder = os.path.join(pathFolder, ""+fileToUpload+"")
                file = open(""+pathFolder+"",'w')
                
                data = serverSocket.recv(4096)
                file.write(data.decode('utf8'))
                file.close()
                
                print('File Uploaded with success')
                
                responseServer='HTTP/1.1 200 OK Uploaded_File_Done'
                sent = serverSocket.sendto(responseServer.encode(), addr)
            
        else:
            print("\n\r The message received is empty")
        
    except:
        print("\n\r Something gone wrong")
    
    
serverSocket.close()
sys.exit()
    
    
    
