#slicing & parsing

data = 'From stepen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print (atpos)
sppos = data.find(' ',atpos)
#print (sppos)
uc = data.upper()
print(uc)
#finding the start of the host name and end of the email host name
host = data[atpos + 1 : sppos]
#print (host)
