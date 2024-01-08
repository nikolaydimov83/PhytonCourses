import re
words=input().split(', ')
result=[]
regex_pattern = r'^[A-Za-z0-9_-]{3,16}$'
for word in words:
    if re.match(regex_pattern,word)!=None:
        result.append(word)
for word in result:
    print(word)