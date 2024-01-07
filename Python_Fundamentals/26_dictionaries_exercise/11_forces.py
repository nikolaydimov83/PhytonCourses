dictionary={}

def create(side, name):
    to_create=False
    user_present=False

    for side_by_side in dictionary.keys():
        if name in dictionary[side_by_side]:
            user_present=True
            break

    if side not in dictionary.keys() and user_present==False:
        dictionary[side]=[name]
    elif side in dictionary.keys() and user_present==False:
        dictionary[side].append(name)
            
    

def change(side, name):
    user_present=False

    for side_by_side in dictionary.keys():
        if name in dictionary[side_by_side]:
            dictionary[side_by_side].remove(name)
            if side in dictionary:
                dictionary[side].append(name)
            else:
                dictionary[side]=[name]

            user_present=True
            print(f"{name} joins the {side} side!")
            break
    if user_present==False:
            if side in dictionary:
                dictionary[side].append(name)
            else:
                dictionary[side]=[name]
            print(f"{name} joins the {side} side!")        


while True:
    command__line=input()
    if command__line=='Lumpawaroo':
        break
    splitted=command__line.split(' -> ')
    if len(splitted)>1:
        side=splitted[1]
        name=splitted[0]
        change(side, name)
    else:
        splitted=command__line.split(' | ')
        side=splitted[0]
        name=splitted[1]        
        create(side, name)

for side, members in dictionary.items():
    if len(members)>0:
        print(f"Side: {side}, Members: {len(members)}")
        for member in members:
            print(f"! {member}")