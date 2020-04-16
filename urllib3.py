#Coursera - 12.4 Retrieving Web Pages

#Using Urllib in PYTHON
#HTTP is very common -- below library does all the SOCKET work for use and makes the .HTM web pages look like a file

# MORE ROBUST CODE

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm') #almost the same as the Open process - gives you file to read. doesn't read it.

for line in fhand: # headers are not in this for loop - you have to ask for them in a different way
    #print (type(line)) # bytes
    print (line.decode().strip()) # take the Byte string from the outside world and conver to unicode string
    #print (type(line)) # strings
