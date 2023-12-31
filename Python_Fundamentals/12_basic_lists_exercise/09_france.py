boundaries={"Clothes":50,"Shoes":35,"Accessories":20.50}
items=input().split('|')
budget=float(input())
initial_budget=budget

sold=[]
profit=0
for i in range(len(items)):
    item_list=items[i].split('->')
    if float(item_list[1])<=boundaries[item_list[0]]:
        if float(item_list[1])<=budget:
            sold.append(str(f"{float(item_list[1])*1.4:.2f}"))
            budget-=float(item_list[1])
            profit+=float(item_list[1])*0.4
print(" ".join(sold))
print(f"Profit: {profit:.2f}")

if (initial_budget+profit>=150):
    print('Hello, France!')
else:
    print('Not enough money.')


