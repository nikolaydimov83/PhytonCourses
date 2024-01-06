def initiate_store(input_line:str):
    bakery_list=input_line.split()
    bakery_dict={}
    for i in range(0,len(bakery_list),2):
        bakery_dict[bakery_list[i]]=int(bakery_list[i+1])
    return bakery_dict

store=initiate_store(input())

keys=input().split()

for key in keys:
    if key in store.keys():
        print(f"We have {store[key]} of {key} left")
    else:
        print(f"Sorry, we don't have {key}")