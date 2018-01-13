import socket
from threading import Thread

s = socket.socket()         # Create a socket object
host = '127.0.0.1'          # Server ip
port = 33555                # Server port

while True:
    try:
        s.connect((host, port))
        break
    except:
        raw_input("Unable to connect to server. Press enter for retry")


print"Connected to server ('" + str(host) + "', " + str(port) + ')'

nickname = raw_input("Enter your nickname: ")
print "Type i + enter for instruction."

def receving():
    while True:
        try:
            print s.recv(1024)
        except:
            print "You are no longer connected to server."
            break
    return


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
    return

#Runs both receving() and sending() at the same time.
try:
    Thread(target = receving).start()
    #Thread(target = sending).start()
    sending()

except:
    print "Error: unable to start thread"

raw_input("Press enter to exit")
