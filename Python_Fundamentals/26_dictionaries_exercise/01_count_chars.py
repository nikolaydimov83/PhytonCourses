string=input()
string.replace(' ','')
dictionary={}
for char in list(string):
    if (char!=' '):
        if char in dictionary:
            dictionary[char]+=1
        else:
            dictionary[char]=1
for char, value in dictionary.items():
    print(f"{char} -> {value}")