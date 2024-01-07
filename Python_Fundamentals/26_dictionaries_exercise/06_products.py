dictionary={}
while True:
    command__line=input()
    if command__line=='buy':
        break
    else:
        name, price, quantity=command__line.split(' ')
        if name not in dictionary:
            dictionary[name]={"price":float(price), "quantity":int(quantity)}
        else:
            dictionary[name]["price"]=float(price)
            dictionary[name]["quantity"]+=int(quantity)

for key, value in dictionary.items():
    
    print(f"{key} -> {(value['quantity']*value['price']):.2f}")