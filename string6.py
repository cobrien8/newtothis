# Find operarter
fruit = 'banana'
pos = fruit.find('na')
print (pos)
#matching strings -- convert strings in comparison to lower and test if they are equal

greet = 'Hello Bob'
nstr = greet.replace('Bob','Jane')
print (nstr)
x = greet.replace('o','x')
print(x)
y = '     Hello bob'
print(y.lstrip()) # lstrip, rstrip and strip - removes white space / spaces
# Starts with Function
if greet.startswith('Hello'):
    print ('Starts with hello!')
