employees_hapiness=input().split(' ')
factor=int(input())
happy_counter=0
factored_hapinees=list(map(lambda x: int(x)* factor,employees_hapiness))
average=sum(factored_hapinees)/len(factored_hapinees)

for i in factored_hapinees:
    if i>=average:
        happy_counter+=1

if happy_counter>=len(factored_hapinees)/2:
    print(f"Score: {happy_counter}/{len(factored_hapinees)}. Employees are happy!")
else:
    print(f"Score: {happy_counter}/{len(factored_hapinees)}. Employees are not happy!")