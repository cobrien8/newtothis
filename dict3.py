counts = dict()
names = ['csev','cwen','csev','zqian','cwen']
for name in names:
    counts[name] = counts.get(name,0)+1 #checks if the 'name' is in the dictionary, if not, assign 0 and add 1
print (counts) #see dict2.py for other example using more code / lines
