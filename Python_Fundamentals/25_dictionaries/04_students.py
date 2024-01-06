university={}
while True:
    command_line=input()
    command_line=command_line.replace('_',' ')
    if command_line in university.keys():
        for course in university[command_line]:
            un_key=list(course.keys())[0]
            un_val=list(course.values())[0]
            print(f"{un_key} - {un_val}")

        break

    else:
        splitted_command_line=command_line.split(":")
        course=splitted_command_line[2]
        name=splitted_command_line[0]
        student_id=splitted_command_line[1]
        if course not in university.keys():
            university[course]=[{name:student_id}]
        else:
            university[course].append({name:student_id})

