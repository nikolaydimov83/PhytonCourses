serachChar='a'

string=input()

for char in string:
    if char==serachChar:
        print('Found '+char)
        break
else:
    print('Char not found')
