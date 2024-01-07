reveresed={}
while True:
    command__line=input()
    if command__line=='end':
        break
    
    rev=list(command__line)
    rev.reverse()
    reveresed[command__line]=''.join(rev)

for key,value in reveresed.items():
    print(f"{key} = {value}")
