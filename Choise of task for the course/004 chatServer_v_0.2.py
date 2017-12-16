import socket
from threading import Thread

s = socket.socket()         # Create a socket object
host = '127.0.0.1'          # Lan ip or localhost (for listening)
port = 33555                # Reserve a port for your service (for listening).
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.

c, addr = s.accept()        # Establish connection with client.

print 'Got connection from', addr
c.send('Successfully established connection to server')

nickname = raw_input("Enter your nickname: ")

def receving():
    while True:
        try:
            print c.recv(1024)
        except:
            print "You are no longer connected to client."
            break

def sending():
    while True:
        try:
            message = raw_input()
            c.send(nickname + ": " + message + " ")
        except:
            break

#Runs both receving() and sending() at the same time.
try:
    Thread(target = receving).start()
    Thread(target = sending).start()
    #sending()

except:
    print "Error: unable to start thread"
