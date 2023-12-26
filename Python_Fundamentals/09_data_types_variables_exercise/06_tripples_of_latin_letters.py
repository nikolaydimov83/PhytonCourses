n=int(input())
list = []
for i in range(n):
    for j in range(n):
        for k in range(n):
           string=chr(97+i)+chr(97+j)+chr(97+k)
           list.append(string) 
for i in list:
    print(i)