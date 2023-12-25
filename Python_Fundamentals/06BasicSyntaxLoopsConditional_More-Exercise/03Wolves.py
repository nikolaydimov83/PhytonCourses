queue=input().split(', ')

if(queue[len(queue)-1]=='wolf'):
    print("Please go away and stop eating my sheep")
else:
    for i in range(len(queue)):
        if(queue[i]=='wolf'):
            print(f"Oi! Sheep number {len(queue)-(i+1)}! You are about to be eaten by a wolf!")