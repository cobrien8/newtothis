fruit = 'banana'
print (fruit[1] + fruit[3] + fruit[5]) # prints the second character (indexing starts at 0)
x = len(fruit)
print (x)
index = 0
print ('Using While to iterate through index of word:')
while index < len(fruit): # does the same as the below for loop and easier for others to read / more simple!
    y = fruit[index] # defining y for fruit index for below code as well
    print (index, y)
    index = index + 1
print('Using for Loop: ')
for y in fruit:
    print (y)
print ('Count letter a in a string')
count = 0
for y in fruit:
    if y == 'a':
       count = count + 1
print (count)
