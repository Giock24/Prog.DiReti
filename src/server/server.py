import os
import sys
import time
import socket as sk

# this method return a list of all file that are present on Server
def listingFiles():
    lista = os.listdir(os.path.join(os.getcwd(), "serverStorage"))
    return lista

#serverPort = 10000
serverSocket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM);

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
                
                sent = serverSocket.sendto(lista.__str__().encode('utf8'), addr)
                
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
                
            elif command == "download":
                
                lista = listingFiles()
                sent = serverSocket.sendto(lista.__str__().encode('utf8'), addr)
                
                print("Waiting the choosing of file to download...")
                data = serverSocket.recv(4096)
                file = data.decode('utf8')
                
                pathFolder = os.path.join(os.getcwd(),"serverStorage")
                pathFolder = os.path.join(pathFolder, ""+file+"")
                
                if os.path.exists(pathFolder):
                    
                    responseServer='HTTP/1.1 200 OK File_Exist'
                    sent = serverSocket.sendto(responseServer.encode(), addr)
                    
                    file = open(""+pathFolder+"",'r')
                    sent = serverSocket.sendto(file.read().__str__().encode('utf8'), addr)
                    time.sleep(2)
                    
                    responseServer='HTTP/1.1 200 OK File_Exist'
                    sent = serverSocket.sendto(responseServer.encode(), addr)
                    
                    
                else:
                    time.sleep(2)
                    responseServer='HTTP/1.1 404 Error File_Not_Found'
                    sent = serverSocket.sendto(responseServer.encode(), addr)
            
        else:
            print("\n\r The message received is empty")
        
    except Exception as e:
        responseServer = 'HTTP/1.1 500 Internal_Server_Error'
        sent = serverSocket.sendto(responseServer.encode('utf8'), addr)
        
        print(e)
        
        serverSocket.close()
        sys.exit()
        
