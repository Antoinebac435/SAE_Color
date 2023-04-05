# coding: utf-8
#Si on crÃ©er la partie 

import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.bind(('', 15555))

while True:
        socket.listen(5)
        client, address = socket.accept()
        print ("{} connected".format( address ))

        response = client.recv(255).decode()
        if response != "":
            print(response)
            client.sendall(b"Oui")
            
            
  
       
print ("Close")
client.close()
stock.close()

