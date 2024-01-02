def sum_numbers(x,y):
    return x+y
def subtract(x,y):
    return x-y

def sum_and_subtract(x,y,z):
    return subtract(sum_numbers(x,y),z)

print(sum_and_subtract(int(input()),int(input()),int(input())))