handle = open('Master.txt') # converted master csv to .txt
count = 0
inp = handle.read() # converts entire file into string, and you can count the total # of characters in the file depending on what you want to do
for row in handle:
    count = count + 1
    print ('Line count:', count)
    print (row) will print all of the data
