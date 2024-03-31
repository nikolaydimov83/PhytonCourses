import re
count=int(input())

pattern1 = r'\$[A-Z][a-z]{2,}\$[:][ ]\[(\d{1,999999999})\]\|\[(\d{1,999999999})\]\|\[(\d{1,999999999})\]\|$'
pattern2 = r'\%[A-Z][a-z]{2,}\%[:][ ]\[(\d{1,999999999})\]\|\[(\d{1,999999999})\]\|\[(\d{1,999999999})\]\|$'

# Example strings
strings = [
    "$Request$: [555555]|[73]|[73]|",
    "%Request%: [555555]|[73]|[73]|%Request%: [555555]|[73]|[73]|",
    "%Taggy$: [73]|[73]|[73]|"
]

for i in range (0,count):
    string=input()
    match1 = re.match(pattern1, string)
    match2 = re.match(pattern2, string)
    if match1 or match2:
        final=''
        body=string.split(': ')[1]
        tag=string.split(': ')[0]
        tag=tag.replace('$', '')
        tag=tag.replace('%', '')
        body_array=body.split('|')
        for code in body_array:
            if code=='':
                continue
            code=code.replace('[','')
            code=code.replace(']','')
            final+= chr(int(code))
        print(tag+': '+final)
    else:
        print(f"Valid message not found!")
