dictionary={}
while True:
    command__line=input()
    if command__line=='end':
        break
    course, student= command__line.split(' : ')

    if course in dictionary:
        dictionary[course].append(student)
    else:
        dictionary[course]=[student]
for course, students in dictionary.items():
    print(f"{course}: {len(students)}")
    for student in students:
        print(f"-- {student}")