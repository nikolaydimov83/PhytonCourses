array = [int(x) for x in input().split()]

average=sum(array)/len(array)
result=[]

for i in array:
    if i>average:
        result.append(i)

if len(result)==0:
    print('No')
result.sort(reverse=True)

if len(result)>0 and len(result)<=5:
    print(' '.join(list(map(str,result))))
else:
    print(' '.join(list(map(str,result[0:5]))))



