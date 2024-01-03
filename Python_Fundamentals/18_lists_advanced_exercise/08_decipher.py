input_line=input().split(' ')
output_list=[]

def decipher_word(input_string):
   
    first_letter_code=[]
    next_letters=[]
    for i in input_string:
        if 48<=ord(i)<=57:
            first_letter_code.append(i)
        else:
            next_letters.append(i)
    first_letter=chr(int(''.join(first_letter_code)))
    next_letters[0],next_letters[len(next_letters)-1]=next_letters[len(next_letters)-1],next_letters[0]
    return (first_letter+''.join(next_letters))

for i in input_line:
    output_list.append(decipher_word(i))
print(' '.join(output_list))

