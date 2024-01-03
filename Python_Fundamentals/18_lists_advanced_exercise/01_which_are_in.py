first_line=input().split(', ')
second_line=input().split(', ')
final_line=[]
for first_line_word in first_line:
    for second_line_word in second_line:
        if second_line_word.find(first_line_word)>-1 and first_line_word not in final_line:
            final_line.append(first_line_word)

print(final_line)


