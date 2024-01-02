def find_comon_divs(string):
    number=int(string)
    result=[]
    for i in range(1,int(number/2)+1):
        if number%i==0:
            result.append(i)
    if sum(result)==number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")

find_comon_divs(input())