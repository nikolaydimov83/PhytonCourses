n=int(input())
dictionary={}
messages=[]
for i in range(n):
    command_line=input().split()

    if command_line[0]=='register':
        if command_line[1] in dictionary:
            print(f"ERROR: already registered with plate number {dictionary[command_line[1]]}")
        else:
            dictionary[command_line[1]]=command_line[2]
            print(f"{command_line[1]} registered {command_line[2]} successfully")
    if command_line[0]=='unregister':
        if command_line[1] not in dictionary:
            print(f"ERROR: user {command_line[1]} not found")
        else:
            del dictionary[command_line[1]]
            print(f"{command_line[1]} unregistered successfully")    

for key, value in dictionary.items():
    print(f"{key} => {value}")

    
    