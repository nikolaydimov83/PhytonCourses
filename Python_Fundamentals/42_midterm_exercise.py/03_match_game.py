sequence=input().split(' ')
turn=0
while True:
    if len(sequence)==0:
        print(f"You have won in {turn} turns!")
        break
    user_input=input()
    turn+=1
    command_indices=user_input.split(' ')
    if user_input=='end':
        print("Sorry you lose :(")
        print(' '.join(sequence))
        break
    
    elif min(int(command_indices[0]),int(command_indices[1]))<0 or max(int(command_indices[0]),int(command_indices[1]))>len(sequence)-1 or int(command_indices[0])==int(command_indices[1]):
        index=int(len(sequence)/2)
        sequence.insert(index,f"-{turn}a")
        sequence.insert(index+1,f"-{turn}a")
        print("Invalid input! Adding additional elements to the board")
    else:
        if sequence[int(command_indices[0])]==sequence[int(command_indices[1])]:
            print(f"Congrats! You have found matching elements - {sequence[int(command_indices[0])]}!")
            sequence.pop(max(int(command_indices[0]),int(command_indices[1])))
            sequence.pop(min(int(command_indices[0]),int(command_indices[1])))
        else:
            print("Try again!")