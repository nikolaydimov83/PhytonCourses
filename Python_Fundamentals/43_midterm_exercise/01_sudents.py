import math

students_count=int(input())
course_lectures=int(input())
additional_bonus=int(input())

max_bonus=0
max_attendance=0

for i in range(students_count):
    student_attendances=int(input())
    total_bonus = student_attendances / course_lectures * (5 + additional_bonus)
    if max_bonus<total_bonus:
        max_attendance=student_attendances
        max_bonus=total_bonus

print(f"Max Bonus: {int(math.ceil(max_bonus))}.")
print(f"The student has attended {max_attendance} lectures.")