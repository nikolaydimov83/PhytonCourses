helth=100
bitcoin=0
best_room=''
max_bitcoin=0

rooms=input().split('|')
for index,room in enumerate(rooms):
    user_input=room.split(' ')
    command=user_input[0]
    volume=int(user_input[1])
    if command=="potion":
        old_helth=helth
        helth=min(100,helth+volume)
        print(f"You healed for {helth-old_helth} hp.")
        print(f"Current health: {helth} hp.")
    elif command=="chest":
        if max_bitcoin<volume:
            best_room=index
            max_bitcoin=volume
        bitcoin+=volume
        print(f"You found {volume} bitcoins.")
    else:
        helth-=volume
        if helth<=0:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {index+1}")
            break
        else:
            print(f"You slayed {command}.")
if helth>0:
    print("You've made it!")
    print(f"Bitcoins: {bitcoin}")
    print(f"Health: {helth}")
