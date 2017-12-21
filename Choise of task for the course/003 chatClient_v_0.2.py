import socket
from threading import Thread
s = socket.socket()         # Create a socket object
host = '127.0.0.1'          # Server ip
port = 33555                # Server port

def connectTo():
    try:
        s.connect((host, port))
    except:
        raw_input("Unable to connect to server. Press enter for retry.")
        connectTo()

connectTo()

print s.recv(1024)
nickname = raw_input("Enter your nickname: ")
print "Type i + enter for instruction."

def receving():
    while True:
        try:
            print s.recv(1024)
        except:
            print "You are no longer connected to server."
            break


def sending():
    while True:
        try:
            message = raw_input()
            if message == "i":
                print "Instruction: If you receive a message at the same time as you typing, you can just continue typing, your message will be sent completely. "
                s.send(nickname + ":*" + 'Has entered command "i"' + "* ")
            else:
                s.send(nickname + ": " + message + " ")
        except:
            break

#Runs both receving() and sending() at the same time.
try:
    Thread(target = receving).start()
    Thread(target = sending).start()
    #sending()

except:
    print "Error: unable to start thread"
