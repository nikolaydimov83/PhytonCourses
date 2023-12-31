def convert_to_list(string):
    return list(map(lambda x:int(x),string.split(' ')))

string = input()
list = convert_to_list(string)

print(f"The minimum number is {min(list)}")
print(f"The maximum number is {max(list)}")
print(f"The sum number is: {sum(list)}")

