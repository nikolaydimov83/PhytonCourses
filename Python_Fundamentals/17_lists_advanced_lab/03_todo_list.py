to_do_list=[]
while True:
    command_line=input()
    if command_line=='End':
        break
    else:
        priority=int(command_line.split('-')[0])
        task=command_line.split('-')[1]
        to_do_list.append({"priority":priority,"task":task})
to_do_list.sort(key=lambda a: a["priority"])
print(list(map(lambda x:x['task'],to_do_list)))