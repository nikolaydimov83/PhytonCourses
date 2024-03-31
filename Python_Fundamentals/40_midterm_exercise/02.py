array=[int(i) for i in input().split(' ')]
index1=-1
index2=-1
def swapF(i1,i2):
    array[i1],array[i2]=array[i2],array[i1]
def multiplyF(i1,i2):
    array[i1]=array[i1]*array[i2]
action={'swap':swapF, 'multiply':multiplyF }
while True:
    command=input()
    if command=='end':
        break
    command_splitted=command.split(' ')
    if (command_splitted[0]!='decrease'):
        index1=int(command_splitted[1])
        index2=int(command_splitted[2])
        action[command_splitted[0]](index1,index2)
    else:
        array=list(map(lambda x:x-1,array))

print(', '.join(list(map(str,array))))


