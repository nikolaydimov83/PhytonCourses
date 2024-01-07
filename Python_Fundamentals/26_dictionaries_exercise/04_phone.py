dictionary={}
counter=0
counter_ceil=0
while True:
    command_line=input().split('-')

    if len(command_line)==1 and counter==0:
        counter_ceil=int(command_line[0])
        counter+=1
        continue
    if len(command_line)==1:
        if command_line[0] in dictionary:
            print(f"{command_line[0]} -> {dictionary[command_line[0]]}")
        else:
            print(f"Contact {command_line[0]} does not exist.")

        counter+=1
        if counter-1==counter_ceil:
            break
    else:
        dictionary[command_line[0]]=command_line[1]