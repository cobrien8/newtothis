counts = dict()
names = ['csev','cwen','csev','zqian','cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print (counts)

# get method apart of dictionaries! use .get after dictionary name

if name in counts:
    x = count[name]
else:
    x = 0
x = count.get(name,0) #won't give a traceback -- use this method to lookup the value
# 0 above becomes the default value if the value does not exist in the dictionary you test
