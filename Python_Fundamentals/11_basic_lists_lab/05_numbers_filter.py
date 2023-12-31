numbers_count = int(input())
numbers_odd_list=[]
numbers_even_list=[]

numbers_negative_list=[]
numbers_positive_list=[]
for i in range(numbers_count):
    number = (int(input()))
    if number%2==0:
        numbers_even_list.append(number)
    else:
        numbers_odd_list.append(number)

    if (number<0):
        numbers_negative_list.append(number)
    else:
        numbers_positive_list.append(number)

command_actions={"even":numbers_even_list, "odd":numbers_odd_list,"negative":numbers_negative_list,"positive":numbers_positive_list}
print(command_actions[input()])