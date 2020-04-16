# Dictionaries part 3! wrapping it all up
# In example - using words.txt file from Coursera

name = input('Enter file name:')
handle = open(name)
counts = dict()

for line in handle:  # create histogram of words in counts dictionary
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0)+1

bigcount = None
bigword = None

for word,count in counts.items(): #for key and value in counts (items returns full list of key and values) check if biggest count and big word
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print (bigword,bigcount)
