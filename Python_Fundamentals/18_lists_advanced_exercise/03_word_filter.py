filtered_list=[word for word in input().split(' ') if len(word)%2==0]
for word in filtered_list:
    print(word)