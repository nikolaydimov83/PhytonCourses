low_bound=int(input())
high_bound=int(input())
string=""

for i in range(low_bound,high_bound+1):
    string+=chr(i)
    if i!=high_bound:
        string+=' '
print(string)