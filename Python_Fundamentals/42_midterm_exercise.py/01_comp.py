command=''
sum_without_tax=0
while True:
    command=input()
    if command in ['special','regular']:
        break
    price=float(command)
    if price<=0:
        print('Invalid price!')
    else:
        sum_without_tax+=price

tax=0.2*sum_without_tax
discount_factor=1
if command=='special':
    discount_factor=0.9
final=(sum_without_tax+tax)*discount_factor

if final==0:
    print("Invalid order!")
else:
    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {sum_without_tax:.2f}$")
    print(f"Taxes: {tax:.2f}$")
    print('-----------')
    print(f"Total price: {final:.2f}$")
