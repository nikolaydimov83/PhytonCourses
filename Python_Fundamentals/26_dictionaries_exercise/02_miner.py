dictionary={}
while True:
    type=input()
    
    if type=='stop':
        break    
    
    quantity=int(input())
    


    if type in dictionary:
        dictionary[type]+=quantity
    else:
        dictionary[type]=quantity

for char, value in dictionary.items():
    print(f"{char} -> {value}")

