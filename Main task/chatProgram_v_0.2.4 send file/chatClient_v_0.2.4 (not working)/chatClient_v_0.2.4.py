import socket
from threading import Thread
import os
if not os.path.exists("Send and receive files folder"):
    os.mkdir("Send and receive files folder")
else:
    pass

while True:
    s = socket.socket()
    host = '127.0.0.1'          # Server ip (for connect to)
    port = 33555                # Server port (for connect to)

    while True:
        try:
            s.connect((host, port))
            break
        except:
            raw_input("Unable to connect to server. Press enter for retry.")
    hostIp = socket.gethostbyname(host)
    print"Connected to server ('" + str(hostIp) + "', " + str(port) + ')'
    nickname = raw_input("Enter your nickname: ")
    s.send(nickname)
    opnickname = s.recv(1024)

    print "Type i + enter for instruction."

    def receving():
        while True:
            try:
                data = s.recv(1024)
            except:
                print "You are no longer connected to server. If you want to try reconnect press enter."
                break
            if data == opnickname + ": " + "-s" + " ":
                print"Other person typed -s. Starting receive a file function"
                fileName = s.recv(1024)
                localFileName = open("Send and receive files folder/" + fileName, 'wb')
                print"File open"
                bytesReceived = s.recv(4096)
                print"Bytes received"
                localFileName.write(bytesReceived)
                print"Bytes write"
                while bytesReceived != "":
                    print"Loop started. The next code line is Bytes receive"
                    bytesReceived = s.recv(4096)  #This is the place where the receive a file process stops.
                    print"Bytes received in loop"
                    localFileName.write(bytesReceived)
                    print"Bytes write in loop"
                localFileName.close()
                print"You received a file from " + nickname + " "
            else:
                print data
        return

    def sending():
        while True:
            try:
                message = raw_input()
                s.send(nickname + ": " + message + " ")
            except:
                break
            if message == "i":
                print "Instruction: If you receive a message at the same time as you typing, you can just continue typing, your message will be sent completely.\nType -s + enter for send a file. "
                s.send(nickname + ":*" + 'Has entered command "i"' + "* ")
            elif message == "-s":
                fileName = raw_input("Enter filename: ")
                while True:
                    if os.path.exists("Send and receive files folder/" + fileName):
                        break
                    else:
                        print'Filename: "' + fileName + '"' + " does not exist "
                        fileName = raw_input()
                s.send(fileName)
                localFileName = open("Send and receive files folder/" + fileName, 'rb')
                bytesToSend = localFileName.read(4096)
                s.send(bytesToSend)
                while bytesToSend != "":
                    bytesToSend = localFileName.read(4096)
                    s.send(bytesToSend)
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
