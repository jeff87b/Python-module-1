import socket
from threading import Thread
import os
if not os.path.exists("Send and receive files folder"):
    os.mkdir("Send and receive files folder")
else:
    pass

while True:
    s = socket.socket()
    host = '127.0.0.1'          # Lan ip or localhost (for listening)
    port = 33555                # Server port (for listening)
    s.bind((host, port))

    s.listen(1)
    print"Listening for incoming connection"

    c, addr = s.accept()
    print 'Got connection from', addr

    nickname = raw_input("Enter your nickname: ")
    opnickname = c.recv(64)
    c.send(nickname)


    def receving():
        while True:
            try:
                data = c.recv(1024)
            except:
                print "You are no longer connected to client. If you want to try reconnect press enter."
                break
            if data == opnickname + ": " + "-s" + " ":
                fileName = c.recv(1024)
                localFileName = open("Send and receive files folder/" + fileName, 'wb')
                bytesReceived = c.recv(4096)
                localFileName.write(bytesReceived)
                while bytesReceived != "":
                    bytesReceived = c.recv(4096)
                    localFileName.write(bytesReceived)
                localFileName.close()
                print"You received a file from " + opnickname + " "
            else:
                print data

        return

    def sending():
        while True:
            try:
                message = raw_input()
                c.send(nickname + ": " + message + " ")
            except:
                break
            if message == "-s":
                fileName = raw_input("Enter filename: ")
                while True:
                    if os.path.exists("Send and receive files folder/" + fileName):
                        break
                    else:
                        print'Filename: "' + fileName + '"' + " does not exist "
                        fileName = raw_input()
                c.send(fileName)
                localFileName = open("Send and receive files folder/" + fileName, 'rb')
                bytesToSend = localFileName.read(4096)
                c.send(bytesToSend)
                while bytesToSend != "":
                    bytesToSend = localFileName.read(4096)
                    c.send(bytesToSend)
                localFileName.close()
                print"Transfer complete "
            else:
                pass
        return

    #Runs both receving() and sending() at the same time.
    try:
        Thread(target = receving).start()
        #Thread(target = sending).start()
        sending()
    except:
        print "Error: unable to start thread"
    s.close()
