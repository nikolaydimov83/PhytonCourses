def split_to_list(string):
    straight=list(string)
    reversed=straight.copy()
    (reversed.reverse())
    if ''.join(reversed)==''.join(string):
        return True
    
    else:
        return False
    
list_of_strings=input().split(', ')
list_of_ints= list(map(lambda x:int(x), list_of_strings))

for i in range(len(list_of_strings)):
    print(split_to_list(list_of_strings[i]))