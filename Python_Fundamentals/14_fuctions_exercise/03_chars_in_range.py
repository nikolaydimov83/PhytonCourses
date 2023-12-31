def chars_in_range(first_char,second_char)->str:
    ascii_first=ord(first_char)
    ascii_second=ord(second_char)
    result=[]
    for i in range(ascii_first+1, ascii_second):
        result.append(chr(i))
    return ' '.join(result)

print(chars_in_range(input(), input()))
