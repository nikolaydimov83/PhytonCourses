people=int(input())
lift=[int(i) for i in input().split(' ')]
final_lift=[]
for carriage in lift:
    if people+carriage<=4:
        carriage=people+carriage
        people=0
    else:
        people-=(4-carriage)
        carriage=4
    final_lift.append(carriage)
if people==0:
    if final_lift[len(final_lift)-1]<4:
        print("The lift has empty spots!")
else:
  print(f"There isn't enough space! {people} people in a queue!") 
print(' '.join(list(map(str, final_lift))))

