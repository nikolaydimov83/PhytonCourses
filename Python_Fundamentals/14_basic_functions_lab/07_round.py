def round_1(string:str)->list:
    return list(map(lambda x:round(float(x)),string.split()))

print(round_1(input()))
