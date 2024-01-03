import math

numbers_list=list(map(int,input().split(', ')))
result={}
max_key=0
for i in numbers_list:
    key=int(math.ceil(i/10))
    if key>max_key:
        max_key=key
    if str(key) not in result:
        result[str(key)]=[i]
    else:
        result[str(key)].append(i)
        
for i in range(10, max_key*10+1,10):
        if str(str(int(i/10))) not in result:
            print(f"Group of {int(i)}'s: {[]}")
        else:
            print(f"Group of {int(i)}'s: {result[str(int(i/10))]}")
    
