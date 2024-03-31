array=input().split('!')
def urgentF(item,dummy):
    if item not in array:
        array.insert(0,item)
def unnecessaryF(item,dummy):
    if item in array:
        array.remove(item)
def correctF(item1, item2):
    if item1 in array:
        index=array.index(item1)
        array[index]=item2
def rearangeF(item,dummy):
    if item in array:
        index=array.index(item)
        popped=array.pop(index)
        array.append(popped)
action={"Urgent":urgentF,'Unnecessary':unnecessaryF,'Correct':correctF,"Rearrange":rearangeF}
item1=False
item2=False

while True:
    user_input=input().split(' ')
    if user_input[0]=="Go" and user_input[1]=='Shopping!':
        break
    command = user_input[0]
    item1=user_input[1]
    if len(user_input)>2:
        item2=user_input[2]
    action[command](item1,item2)

print(', '.join(array))
