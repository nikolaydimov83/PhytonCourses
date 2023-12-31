def abs_value(list_values_str:str) ->list:
    
    list_int=list(map(str_to_float_absoluted,list_values_str.split(' ')))

    
    return list_int
def str_to_float_absoluted(str:str)->int:
    return abs(float(str))

list_values_str=input()

print(abs_value(list_values_str))