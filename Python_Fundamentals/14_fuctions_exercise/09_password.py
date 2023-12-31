def pass_len(password):
    if len(password)>=6 and len(password)<=10:
        return True
    else:
        return False
def only_nums_only_digits(password):
    list_chars=list(password)
    for char in list_chars:
        if 48<=ord(char)<=57 or 65<=ord(char)<=90 or 97<=ord(char)<=122:
            a=5
        else:
            return False
    return True
def min_two_digits(password):
    list_chars=list(password)
    count_digits=0
    for char in list_chars:
        if 48<=ord(char)<=57:
            count_digits+=1
    if count_digits>=2:
        return True
    else:
        return False
    
password=input()

if pass_len(password) and only_nums_only_digits(password) and min_two_digits(password):
    print("Password is valid")
if pass_len(password)==False:
    print("Password must be between 6 and 10 characters")
if only_nums_only_digits(password)==False:
    print("Password must consist only of letters and digits")
if min_two_digits(password)==False:
    print("Password must have at least 2 digits")
