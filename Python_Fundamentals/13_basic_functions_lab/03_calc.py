

def calc(operator, x, y):
    calc_object={
        'multiply':lambda x,y:x*y, 
        'divide':lambda x,y:int(x/y), 
        'add':lambda x,y:(x+y), 
        'subtract':lambda x,y:x-y}
    return calc_object[operator](int(x),int(y))

print(calc(input(), input(), input()))