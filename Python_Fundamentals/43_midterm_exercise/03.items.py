items=input().split(', ')

def collect(item):
    if item not in items:
        items.append(item)
def drop(item):
    if item in items:
        items.remove(item)
def combine(item):
    old,new=item.split(':')
    if old in items:
        index=items.index(old)
        items.insert(index+1,new)
def renew(item):
    if item in items:
        index=items.index(item)
        items.pop(index)
        items.append(item)

action={"Collect":collect,"Drop":drop,"Combine Items":combine,"Renew":renew}

while True:
    user_input=input()
    if user_input=="Craft!":
        break

    command,item_u=user_input.split(" - ")
    action[command](item_u)

print(', '.join(items))