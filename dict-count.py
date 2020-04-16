# Dictiories part 3 lesson

# Counting Pattern:
counts = dict()
print ('Enter a line of text:')
line = input('')
words = line.split() # split the text entered by spaces
print ('Words:' , words) # prints out the split words
print ('Counting....')
for word in words:
    counts[word] = counts.get(word,0) + 1 # checks if word in dict, if not add w/ value of 0 and add 1
print ('Counts are:', counts)
