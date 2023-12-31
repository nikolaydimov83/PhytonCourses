number_strings = int(input())
search_word=input()
all_list=[]
serach_list=[]
for i in range(number_strings):
    string=input()
    all_list.append(string)

    if(string.find(search_word)>-1):
        serach_list.append(string)
print(all_list)
print(serach_list)

