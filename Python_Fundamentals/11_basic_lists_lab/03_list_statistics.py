input_count=int(input())
positives=[]
negatives=[]

for i in range(input_count):
    number=int(input())
    if number>=0:
        positives.append(number)
    if number<0:
        negatives.append(number)
print(positives)
print(negatives)
print(f"Count of positives: {len(positives)}")
print(f"Sum of negatives: {sum(negatives)}")