def sum_ods_evens(number:int):
    number_list=list(map(lambda num:int(num),list(str(number))))
    sum_ods=0
    sum_evens=0
    for i in number_list:
        if i%2==0:
            sum_evens+=i
        else:
            sum_ods+=i
    print(f"Odd sum = {sum_ods}, Even sum = {sum_evens}")

sum_ods_evens(int(input()))

