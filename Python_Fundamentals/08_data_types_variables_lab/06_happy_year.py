year=int(input())
new_year=year+1
while True:
    
    new_year_list=list(str(new_year))
    yearOK=False
    for i in range(len(new_year_list)):
        altered_list=new_year_list[:i] + new_year_list[i + 1:]
        if new_year_list[i] in altered_list:
            break
        elif i==len(new_year_list)-1:
            yearOK=True
    if yearOK:
        print(new_year)
        break
    else:
        new_year+=1