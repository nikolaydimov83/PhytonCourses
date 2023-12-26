lines=int(input())
capacity=255
total_water=0

for i in range(lines):
    current_water=int(input())
    if (total_water+current_water>capacity):
        print("Insufficient capacity!")
    else:
        total_water+=current_water
print(total_water)