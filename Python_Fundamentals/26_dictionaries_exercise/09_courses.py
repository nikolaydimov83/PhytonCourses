rows=int(input())
dictionary={}

for _ in range(rows):
    studen=input()
    grade=float(input())
    if studen in dictionary:
        dictionary[studen].append(grade)
    else:
        dictionary[studen]=[grade]
for student, grades in dictionary.items():
    averageGrade=sum(grades)/len(grades)
    if averageGrade>=4.50:
        print(f"{student} -> {averageGrade:.2f}")