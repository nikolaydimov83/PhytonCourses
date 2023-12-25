coffee_structure = {
    'dog': 1,
    'cat': 1,
    'movie': 1,
    'coding':1,
    'DOG': 2,
    'CAT': 2,
    'MOVIE': 2,
    'CODING':2
}

totalCoffes=0

while True:
    command=input()
    if command=='END':
        break
    else:
        currentCoffes=coffee_structure.get(command, 0)
        totalCoffes+=currentCoffes
if totalCoffes>5:
    print("You need extra sleep")
else:
    print(totalCoffes)
