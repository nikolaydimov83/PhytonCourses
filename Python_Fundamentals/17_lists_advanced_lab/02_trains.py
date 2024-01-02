train = [0 for i in range(int(input()))]
def add(guantity):
    train[len(train)-1]+=guantity
def insert(index, quantity):
    train[index]+=quantity
def leave(index, quantity):
    train[index]-=quantity

actions={'add':add, 'insert':insert, 'leave':leave}



while True:
    command_line=input().split(' ')
    command=command_line[0]
    if command=='End':
        break
    index=int(command_line[1])
    
    if command=='End':
        break
    if command=='add':
        actions['add'](index)
        continue
    
    quantity=int(command_line[2])
    actions[command](index,quantity)

print(train)

