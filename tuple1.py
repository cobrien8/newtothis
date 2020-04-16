#Tuples section of Coursera

#Sorting by values (K,V) of a tuple instead of by the key
#sorted(dictionary.items()) will sort the keys

c = {'a':10, 'b':1, 'c':22}
tmp = list()
for k,v in c.items():
    tmp.append( (v,k) ) #append empty list with the reverse of key values

print(tmp)
tmp = sorted(tmp,reverse = True)
print(tmp)
