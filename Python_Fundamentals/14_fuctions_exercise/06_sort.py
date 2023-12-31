def sort1(string:str):
    return sorted(string.split(),key=lambda x:int(x))
    
print(list(map(lambda x: int(x),sort1(input()))))
