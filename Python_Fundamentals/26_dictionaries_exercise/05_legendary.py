dictionary={}
break_flag=False
while True:   
    if break_flag==True:
        break 
    command_line=input().split(' ')

    for i in range(0,len(command_line), 2):
        if command_line[i+1] not in dictionary:
            dictionary[command_line[i+1]]=int(command_line[i])  
        else:
            dictionary[command_line[i+1]]+=int(command_line[command_line[i]]) 
        if dictionary[command_line[i+1]]>=250:
            print(f"{command_line[i+1]} obtained!")
            break_flag=True
            break

print(f"shards: {dictionary.shards}")
print(f"fragments: {dictionary.fragments}")
print(f"motes: {dictionary.motes}")