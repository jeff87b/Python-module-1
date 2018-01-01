import socket
import os
if not os.path.exists("Send and receive files folder"):
    os.mkdir("Send and receive files folder")
else:
    pass
s = socket.socket()
host = '127.0.0.1'
port = 33555

s.bind((host, port))

s.listen(1)
print"Listening for incoming connection"

c, addr = s.accept()
print 'Got connection from', addr

def send():
    fileName = raw_input("Enter filename: ")
    c.send(fileName)
    localFileName = open("Send and receive files folder/" + fileName, 'rb')
    bytesToSend = localFileName.read(4096)
    c.send(bytesToSend)
    while bytesToSend != "":
        bytesToSend = localFileName.read(4096)
        c.send(bytesToSend)
    localFileName.close()
    print"Transfer complete "

send()
