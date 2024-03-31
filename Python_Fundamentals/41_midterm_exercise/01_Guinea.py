food=float(input())
hay=float(input())
cover=float(input())
weight=float(input())
message='No message'

for i in range(1,31):
    food-=0.3
    if (i%2==0):
        hay-=0.05*food
    if i%3==0:
        cover-=weight/3
    if (food==0 or hay==0 or cover==0) and i!=30:
        message=("Merry must go to the pet store!")
        break
if (food<0 or hay<0 or cover<0):
    message=("Merry must go to the pet store!")


if message=='No message':
    print(f"Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.")
else:
    print(message)

