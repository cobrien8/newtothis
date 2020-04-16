# Looping through dictionary of tuples to count 10 most common words

fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1 #Makes historgram of the words in romeo.text

# The below section can be done EVEN shorter - using list comprehension in python
# simply - print(sorted([(v,k) for k,v in c.items()]reverse=True)) - makes three tuples flipped


lst = list()
for k,v in counts.items():
    newtup = (v,k)
    lst.append(newtup)

lst = sorted(lst,reverse=True) #sorts in descending order
for v,k in lst[:10]: #prints top ten (flipped) most common words
    print (k,v) #print it out in the order we wanted in the first place
