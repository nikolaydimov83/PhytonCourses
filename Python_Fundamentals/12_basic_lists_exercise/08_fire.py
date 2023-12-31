boundaries={"High":{"min":81, "max":125},"Medium":{"min":51,"max":80},"Low":{"min":1, "max":50}}
fires= input().split('#')
water=int(input())
cells=[]
total_fire=0
effort=0

for i in range(len(fires)):
    fire_details=fires[i].split(' = ')
    if int(fire_details[1])>= boundaries[fire_details[0]]["min"] and int(fire_details[1])<= boundaries[fire_details[0]]["max"]:
        if int(fire_details[1])<=water:
            water-=int(fire_details[1])
            cells.append(int(fire_details[1]))
            total_fire+=int(fire_details[1])
            effort+=0.25*int(fire_details[1])
print("Cells:")

for i in range(len(cells)):
    print(f' - {cells[i]}')
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")