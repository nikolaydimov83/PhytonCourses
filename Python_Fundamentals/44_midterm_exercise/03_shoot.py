array=[int(i) for i in input().split()]


def shoot(index,power):
    if index>=0 and index<len(array):
        if power>=array[index]:
            array.pop(index)
        else:
            array[index]-=power
def add(index, value):
    if index>=0 and index<len(array):
        array.insert(index,value)
    else:
        print("Invalid placement!")
def strike(index, radius):
    global array
    if (index-radius>=0) and ((index+radius)<len(array)):
      
        array1=array[0:index-radius]
        array2=array[index+radius+1:]
        array=array1+array2
    else:
        print("Strike missed!")
action={"Shoot":shoot,"Add":add,"Strike":strike}

while True:
    user_input=input()
    if user_input=="End":
        break
    command,item1, item2=user_input.split(' ')
    action[command](int(item1),int(item2))
print('|'.join(list(map(str,array))))
