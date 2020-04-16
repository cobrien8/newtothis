#Coursera - 12.4 Retrieving Web Pages

#Using Urllib in PYTHON
#HTTP is very common -- below library does all the SOCKET work for use and makes the .TXT web pages look like a file

# MORE ROBUST CODE

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt') #almost the same as the Open process - gives you file to read. doesn't read it.
counts = dict()
for line in fhand:
    print (type(line)) # bytes
    words = line.decode().split()# take the Byte string from the outside world and conver to unicode string
    for word in words:
        print (type(word)) # strings
        counts[word] = counts.get(word,0) + 1
print (counts)
