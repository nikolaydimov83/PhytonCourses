rounds=int(input())
surplus=0
rooms_with_lack=False
messages=[]
for i in range(rounds):
    room=input().split(' ')
    lack=int(room[1])-len(room[0])
    if (lack>0):
        
        messages.append(f"{lack} more chairs needed in room {i+1}")
        rooms_with_lack=True
    else:
        surplus+=abs(lack)
if not rooms_with_lack:
    print(f"Game On, {surplus} free chairs left")
else:
    for i in messages:
        print(i)