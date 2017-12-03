# This is chatClient_v_0.1.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = '127.0.0.1'          # Server IP
port = 33555                # Server port

s.connect((host, port))

print s.recv(1024)

nickname = raw_input("Enter your nickname: ")
while True:
    message = raw_input(nickname + "-> ")
    s.send(nickname + ": " + message)
    print s.recv(1024)

#s.close()                     # Close the socket when done
