animals={}

def add(command):
    splitted_command=command.split('-')
    animal_name=splitted_command[0]
    needed_food_quantity=int(splitted_command[1])
    area=(splitted_command[2])
    if animal_name in list(animals.keys()):
        animals[animal_name]["food"]+=needed_food_quantity
    else:
        animals[animal_name]={"food":needed_food_quantity, "area":area}
def feed(command):
    splitted_command=command.split('-')
    animal_name=splitted_command[0]
    given_food=int(splitted_command[1])
    if animal_name in list(animals.keys()):
        animals[animal_name]["food"]-=given_food
        if animals[animal_name]["food"]<=0:
            print(f"{animal_name} was successfully fed")
            del animals[animal_name]

actions={"Add":add,"Feed":feed}

while (True):
    user_input=input().split(': ')
    if user_input[0]=="EndDay":
        break
    action=user_input[0]
    command=user_input[1]
    actions[action](command)

print("Animals:")
areas={}
for animal_name in list(animals.keys()):
    food="food"
    print(f" {animal_name} -> {animals[animal_name][food]}g")
    if animals[animal_name]["area"] not in areas:
        areas[animals[animal_name]["area"]]=1
    else:
        areas[animals[animal_name]["area"]]+=1

print("Areas with hungry animals:")

for key, value in areas.items():
    print(f" {key}: {value}")


print(bool(""))
print(bool(0))
print(bool(None))
print(bool(-1))


