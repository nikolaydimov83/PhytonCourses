numbers=list(map(lambda x:int(x), input().split(', ')))
positives=[]
negatives=[]
evens=[]
odds=[]
for i in numbers:
    if i>=0:
        positives.append(i)
    else:
        negatives.append(i)
    if i%2==0:
        evens.append(i)
    else:
        odds.append(i)

print("Positive: "+', '.join(map(str,positives)))
print("Negative: "+', '.join(map(str,negatives)))
print("Even: "+', '.join(map(str,evens)))
print("Odd: "+', '.join(map(str,odds)))