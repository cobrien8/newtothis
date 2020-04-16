#Coursera - 12.4 Retrieving Web Pages

#Using Urllib in PYTHON
#HTTP is very common -- below library does all the SOCKET work for use and makes the web pages look like a file


import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt') #almost the same as the Open process - gives you file to read. doesn't read it.
for line in fhand:
    print (line.decode().strip()) #iterates through all lines (byte array so we need to decode it then strip the white space)
