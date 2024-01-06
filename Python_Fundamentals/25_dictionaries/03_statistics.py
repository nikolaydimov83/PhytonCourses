store={}
while True:
    commant_line=input()
    if commant_line=='statistics':
        print("Products in stock:")
        for product in store.keys():
            print(f"- {product}: {store[product]}")
        print(f"Total Products: {len(store.keys())}")
        print(f"Total Quantity: {sum(store.values())}")
        break
    else:
        key_value_input=commant_line.split(': ')
        if key_value_input[0] in store:
            store[key_value_input[0]]+=int(key_value_input[1])
        else:
            store[key_value_input[0]]=int(key_value_input[1])
