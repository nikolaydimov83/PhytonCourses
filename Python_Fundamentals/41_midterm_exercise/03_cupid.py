array=[int(i) for i in input().split('@')]
current_possition=0

while True:
    user_input=input()
    if user_input=='Love!':
        break
    jump_len=int(user_input.split(' ')[1])
    if current_possition+jump_len>len(array)-1:
        current_possition=0
    else:
        current_possition+=jump_len
    if array[current_possition]==0:
        print(f"Place {current_possition} already had Valentine's day.")
    else:
        array[current_possition]-=2
        if array[current_possition]==0:
            print(f"Place {current_possition} has Valentine's day.")

print(f"Cupid's last position was {current_possition}.")
success=True
counter=0
for i in array:
    if i!=0:
        success=False
        counter+=1
        
if success==True:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {counter} places.")
