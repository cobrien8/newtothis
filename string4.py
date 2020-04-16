word = input('choose a word: ')
if word == 'banana':
    print('the word is banana!')
if word < 'banana':
    print('your word,' + word + ', comes before banana')
elif word > 'banana':
    print('your word,' + word + ' , comes after banana')
else:
    print('the word is banana!')
