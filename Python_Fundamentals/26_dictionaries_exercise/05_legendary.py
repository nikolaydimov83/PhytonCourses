dictionary={"shards":0, "fragments":0,"motes":0}
specials={ 
    "shards":"Shadowmourne",
    "fragments":"Valanyr",
    "motes":"Dragonwrath"}
break_flag=False
while True:   
    if break_flag==True:
        break 
    command_line=input().split(' ')

    for i in range(0,len(command_line), 2):
        key = command_line[i+1].lower()
        value=int(command_line[i])
        if key not in dictionary:
            dictionary[key.lower()]=int(value)  
        else:
            dictionary[key.lower()]+=int(value) 
        if dictionary[key]>=250 and key in ['shards','fragments','motes']:
            dictionary[key]-=250
            print(f"{specials[key]} obtained!")
            break_flag=True
            break

print(f"shards: {dictionary['shards']}")
print(f"fragments: {dictionary['fragments']}")
print(f"motes: {dictionary['motes']}")

for item in dictionary.items():
    if item[0] not in ['shards','fragments','motes']:
        print(f"{item[0]}: {item[1]}")
