string=input()
temporary_string=string[0]
result=[]
for i in range(len(string)-1):
    
    if string[i]==string[i+1]:
        temporary_string=temporary_string+string[i+1]
        if i==(len(string)-2):
            result.append(temporary_string)
    else:
        result.append(temporary_string)
        temporary_string=string[i+1]
        if i==(len(string)-2):
            result.append(string[i+1])        

for i in range(len(result)):
    result[i]=result[i].replace(result[i],result[i][0])

print(''.join(result))