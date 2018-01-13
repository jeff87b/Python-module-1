import socket
from threading import Thread

s = socket.socket()         # Create a socket object
host = '127.0.0.1'          # Lan ip or localhost (for listening)
port = 33555                # Server port (for listening)
s.bind((host, port))        # Bind to the port

s.listen(1)                 # Now wait for client connection
print"Listening for incoming connection"

c, addr = s.accept()        # Establish connection with client

print 'Got connection from', addr

nickname = raw_input("Enter your nickname: ")

def receving():
    while True:
        try:
            print c.recv(1024)
        except:
            print "You are no longer connected to client."
            break
    return

def sending():
    while True:
        try:
            message = raw_input()
            c.send(nickname + ": " + message + " ")
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
