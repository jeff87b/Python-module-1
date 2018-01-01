import socket
import os
if not os.path.exists("Send and receive files folder"):
    os.mkdir("Send and receive files folder")
else:
    pass
s = socket.socket()
host = '127.0.0.1'
port = 33555

while True:
    try:
        s.connect((host, port))
        break
    except:
        raw_input("Unable to connect to server. Press enter for retry.")

print"Connected to server ('" + str(host) + "', " + str(port) + ')'

while True:
    while True:
        if 10 > 9:
            fileName = s.recv(1024)
            localFileName = open("Send and receive files folder/" + fileName, 'wb')
            bytesReceived = s.recv(4096)
            localFileName.write(bytesReceived)
            while bytesReceived != "":
                bytesReceived = s.recv(4096)
                localFileName.write(bytesReceived)
            localFileName.close()
            print"You received a file from " + "nickname"
            break

        else:
            pass
    break
