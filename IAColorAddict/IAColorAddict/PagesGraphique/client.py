# coding: utf-8

import socket

hote = "172.20.10.5"
port = 15555

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))
print ("Connection on {}".format(port))

socket.send("Hey my name is Olivier!")

print ("Close")
socket.close()