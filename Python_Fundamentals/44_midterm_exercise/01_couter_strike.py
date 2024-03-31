energy=int(input())
won=False
battles=0

while True:
    command=input()
    if command=="End of battle":
        won=True
        break
    else:
        command=int(command)
        if (energy-command)>=0:
            battles+=1
            energy-=command
            if (battles)%3==0:
                energy+=battles

        else:                    
            print(f"Not enough energy! Game ends with {battles} won battles and {energy} energy")
            break
if won==True:
    print(f"Won battles: {battles}. Energy left: {energy}")
