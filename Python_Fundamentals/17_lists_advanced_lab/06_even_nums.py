evens=[]
def return_even_indice(tupple):
    if int(tupple[1])%2==0:
        evens.append(tupple[0])
        return tupple[0]

list=list(map(lambda x:return_even_indice(x),list(enumerate(input().split(', ')))))
print(evens)