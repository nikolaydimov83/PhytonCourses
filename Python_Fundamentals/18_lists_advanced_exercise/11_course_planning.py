curriculum=input().split(', ')

def add(lesson_tittle,index):
    curriculum.append(lesson_tittle)

def insert(lesson_tittle,index):
    index=int(index)
    if lesson_tittle not in curriculum:
        curriculum.insert(index,lesson_tittle)

def remove(lesson_tittle,index):
    if lesson_tittle in curriculum:
        curriculum.remove(lesson_tittle)

def swap(lesson_tittle1,lesson_tittle2):
    if lesson_tittle1 in curriculum and lesson_tittle2 in curriculum:
        index1=curriculum.index(lesson_tittle1)
        index2=curriculum.index(lesson_tittle2)
        exercise1=''
        exercise2=''
        if f"{lesson_tittle1}-Exercise" in curriculum:
            curriculum.remove(f"{lesson_tittle1}-Exercise")
            exercise1=f"{lesson_tittle1}-Exercise"
        if f"{lesson_tittle2}-Exercise" in curriculum:
            curriculum.remove(f"{lesson_tittle2}-Exercise")
            exercise2=f"{lesson_tittle2}-Exercise"

        curriculum[index1],curriculum[index2]=curriculum[index2],curriculum[index1]
        if exercise1!='':
            index1=curriculum.index(lesson_tittle1)
            curriculum.insert(index1+1,exercise1)
        if exercise2!='':
            index2=curriculum.index(lesson_tittle2)
            curriculum.insert(index2+1,exercise2)        
            

def exercise(lesson_tittle,index):
    if lesson_tittle in curriculum:
        if f"{lesson_tittle}-Exercise" not in curriculum:
            lesson_index=curriculum.index(lesson_tittle)
            curriculum.insert(lesson_index+1,f"{lesson_tittle}-Exercise")
    else:
        curriculum.append(lesson_tittle)
        curriculum.append(f"{lesson_tittle}-Exercise")

action={
        "Add":add, 
        "Insert":insert, 
        "Remove":remove,
        "Swap":swap,
        "Exercise":exercise
        }

while True:
    command_input=input().split(':')
    
    if len(command_input)<=2:
        command_input.append('None')  

    if command_input[0]=="course start":
        break

    if command_input[0]=='Add':
        add(command_input[1], command_input[2])

    if command_input[0]=='Insert':
        insert(command_input[1], command_input[2])    

    if command_input[0]=='Remove':
        remove(command_input[1], command_input[2])

    if command_input[0]=='Swap':
        swap(command_input[1], command_input[2])  
    if command_input[0]=='Exercise':
        exercise(command_input[1], command_input[2])   
for i in enumerate(curriculum):
    print(f"{int(i[0])+1}.{i[1]}")   

    