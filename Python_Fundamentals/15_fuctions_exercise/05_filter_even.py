def filter_evens(string:str):
    list_evens=list(filter(lambda x:int(x)%2==False,string.split(' ')))
    list_evens_ints=list(map(lambda x:int(x),list_evens))
    return list_evens_ints
print(filter_evens(input()))