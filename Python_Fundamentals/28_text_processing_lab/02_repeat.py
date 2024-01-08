line = input().split()
str=''
for word in line:
    str=str+word*len(word)
print(str)