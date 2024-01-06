word_list=list(map(lambda x:x.lower(), input().split(' ')))
word_dict={}

for word in word_list:
    if word in word_dict.keys():
        word_dict[word]+=1
    else:
        word_dict[word]=1
word_dict_final={ key:value for key, value in list(word_dict.items()) if value%2==1}
print(''.join([ key for key in word_dict_final.keys()]))