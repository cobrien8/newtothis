# Definite loops and dictoniries - simple
counts = {'chuck' : 1, 'fred' : 42, 'jan' : 100}
for key in counts:  # going through the keys, not the values in the dictionary
    print(key,counts[key])
print (list(counts)) #only converts the keys to a list and prints the list of keys
print (counts.keys()) #only prints the keys - output is a list
print (counts.values()) #only prints the values - output is a list
print (counts.items()) #prints list of key and value pairs of the dictionary - output is a tuple for each value in the list - tuples are data structures

# for loop to go through key and value pairs
for k,v in counts.items(): #runs through each key,value - key is first iteration variable, value is last
    print(k,v) #prints all the items in the dictionary!
