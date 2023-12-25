last_number=int(input())

for i in range(1,last_number+1):
    number_as_list=list(str(i))
    sum=0
    for j in number_as_list:
        sum+=int(j)
    if (sum==5 or sum==7 or sum==11):
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")
