str1=input()
str2=input()

while True:
    if str1 in str2:
        str2=str2.replace(str1,'')
    else:
        break
print(str2)