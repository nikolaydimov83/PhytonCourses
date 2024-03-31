coffee_array=input().split()
n=int(input())

def include(item):
    coffee_array.append(item)
def remove(input):
    global coffee_array
    command,number=input.split(' ')
    number=int(number)
    if number<=len(coffee_array):
        if command=='first':
            coffee_array=coffee_array[number:]
        else:
            coffee_array=coffee_array[:len(coffee_array)-number]
def prefer(input):
    index1, index2=input.split(' ')
    index1=int(index1)
    index2=int(index2)
    if index1>=0 and index1<len(coffee_array) and index2>=0 and index2<len(coffee_array):
        coffee_array[index1], coffee_array[index2] = coffee_array[index2], coffee_array[index1]
def reverse(input):
    global coffee_array
    coffee_array.reverse()
action={"Include":include, "Remove":remove, "Prefer":prefer,"Reverse":reverse}

for i in range(n):
    user_input=input().split()
    command=user_input[0]
    user_input.pop(0)
    if len(user_input)==0:
        user_input.append('a')
    altered=' '.join(user_input)
    action[command](altered)
print('Coffees:')
print(' '.join(coffee_array))