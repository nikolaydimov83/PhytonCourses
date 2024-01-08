words=input()
result=''
for char in list(words):
    result+=chr(ord(char)+3)
print(result)