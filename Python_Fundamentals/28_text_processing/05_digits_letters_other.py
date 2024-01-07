string_list=list(input())
alpha=[]
nums=[]
others=[]

for char in string_list:
    if char.isalpha():
        alpha.append(char)
    elif char.isdigit():
        nums.append(char)
    else:
        others.append(char)
print("".join(nums))
print("".join(alpha))
print("".join(others))

