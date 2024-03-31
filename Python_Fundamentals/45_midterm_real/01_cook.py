import math
budget=float(input())
students=int(input())
price_flour=float(input())
price_egg=float(input())
price_Apron=float(input())

aprons_cost=(students+math.ceil(0.2*students))*price_Apron
flour_cost=0

for i in range(1,students+1):
    if i%5!=0:
        flour_cost+=price_flour

eggs_cost=price_egg*students*10

if (eggs_cost+aprons_cost+flour_cost<=budget):
    print(f"Items purchased for {eggs_cost+aprons_cost+flour_cost:.2f}$.")
else:
    print(f"{abs(budget-(eggs_cost+aprons_cost+flour_cost)):.2f}$ more needed.")