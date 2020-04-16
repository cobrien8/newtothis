# Coursera Chapter 12 - Networked Technology

# Sockets in PYTHON!!

# Built in support within python for TCP Sockets

import Sockets
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #basically creates an endpoint inside this computer that is ready to connect out to the far end, but is not yet connected
# AF_INET means connect to the internet - and we are going to STREAM means its a series of characters that just keeps coming back
# Returns an object into mysock, then  we call the connect method in that object
mysock.connect( ( 'data.pr4e.org', 80 )) # data.pr4e.org = host / domain, 80 = import

# this just dials the phone and makes the connection!! doesn't grab the data yet or do anything, but make the connection.

# HTTP Request in Python Example


cmd =  'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd) # Have to do a send first to the server -- sending a get request

while True: # use while look for while connected and
    data = mysock.recv(512) #recieve up to 512 characters
    if (len(data) < 1): # if we get no data then we break
        break
    print (data.decode()) #print out the data as it is coming back from the server / interpret what was sent
mysock.close() #close the connection, takes up resources on both computers

# output will be strings
