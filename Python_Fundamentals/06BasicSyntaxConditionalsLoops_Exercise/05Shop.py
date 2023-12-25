numberOfOrders=int(input())
total=0
for i in range(numberOfOrders):
    price= float(input())#float(f"{float(input()):.2f}")
    days=int(input())
    capsules=int(input())
    
    if (0.01<=price<=100) and (1<=days<=31) and (1<=capsules<=2000):
        total+=price*days*capsules
        print(f"The price for the coffee is: ${f'{price*days*capsules:2.2f}'}")
    else:
        continue
print(f"Total: ${total:2.2f}")

