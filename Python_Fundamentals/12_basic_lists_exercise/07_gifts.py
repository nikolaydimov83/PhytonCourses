gifts_list=input().split()

while True:
    command=input()
    if command=="No Money":
        break
    command_list=command.split(' ')
    if command_list[0]=='OutOfStock':
        if (command_list[1] in gifts_list):
           
            start_index=0
            while True:
                try:
                    index_to_change=gifts_list.index(command_list[1],start_index)
                    gifts_list[index_to_change]=None
                    start_index=index_to_change+1
                except Exception as e:
                    break
    if command_list[0]=='Required':
        if 0<=int(command_list[2])<len(gifts_list):
            gifts_list[int(command_list[2])]=command_list[1]
    if command_list[0]=='JustInCase':
        gifts_list[len(gifts_list)-1]=command_list[1]
final=[]
for i in range(len(gifts_list)):
    if gifts_list[i]!=None:
        final.append(gifts_list[i])
print(" ".join(final))

