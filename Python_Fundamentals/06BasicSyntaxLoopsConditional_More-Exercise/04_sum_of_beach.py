input_string=input()
magic_words=['water', 'sand', 'fish', 'sun']
counter=0
for i in magic_words:
    itterated_string=input_string
    while len(itterated_string)>=len(i):
        if (itterated_string.lower().find(i)>-1):
            counter+=1
            itterated_string=itterated_string[itterated_string.lower().find(i)+len(i):]
        else:
            break

print(counter)