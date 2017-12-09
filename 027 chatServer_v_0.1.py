# This is chatServer_v_0.1.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = '127.0.0.1'          # Lan ip or localhost (for listening)
port = 33555                # Reserve a port for your service (for listening).
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.

c, addr = s.accept()     # Establish connection with client.
print 'Got connection from', addr
c.send('Successfully established connection to server')

nickname = raw_input("Enter your nickname: ")
while True:
    print c.recv(1024)
    message = raw_input(nickname + "-> ")
    c.send(nickname + ": " + message)

#c.close()                # Close the connection
