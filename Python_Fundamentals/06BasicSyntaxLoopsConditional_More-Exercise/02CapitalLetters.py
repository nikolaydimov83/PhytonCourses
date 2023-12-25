list_chars=list(input())
list_indexes_cap_letters=[]

for i in range(len(list_chars)):
    if(ord(list_chars[i])>=65 and ord(list_chars[i])<=90):
        list_indexes_cap_letters.append(i)

print(list_indexes_cap_letters)