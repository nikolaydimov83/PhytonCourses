while True:
    string = input()
    if string=="End":
        break
    elif string=='SoftUni':
        continue
    else:
        for i in string:
            print(i+i,end='')
        print()

