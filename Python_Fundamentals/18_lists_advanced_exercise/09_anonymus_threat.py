import math
input_list=input().split(' ')
def merge(start,end,input_list_local):
    if end>(len(input_list_local)-1):
        end=len(input_list_local)-1
    if start<0:
        start=0
    medium_list=input_list_local[start:end+1]
    medium_string=''.join(medium_list)
    start_list=input_list_local[0:start]
    end_list=input_list_local[end+1:len(input_list_local)]
    start_list.append(medium_string)
    start_list.extend(end_list)
    input_list_local=start_list.copy()
    return input_list_local

def divide(index, clusters_count,input_list_local):
    if index>(len(input_list_local)-1):
        index=len(input_list_local)-1
    if index<0:
        index=0
    string_to_divide=input_list_local[index]
    length_string=len(string_to_divide)
    cluster_size=int(math.floor(length_string/clusters_count))
    cluster_remainder=length_string%clusters_count+cluster_size

    medium_list=[]
    while len(string_to_divide)>cluster_remainder:
        medium_list.append(string_to_divide[0:cluster_size])
        string_to_divide=string_to_divide[cluster_size:]
    medium_list.append(string_to_divide)
    result=[]
    result=input_list_local[:index]
    result.extend(medium_list)
    result.extend(input_list_local[index+1:])
    return result
action={"merge":merge,"divide":divide}


while True:
    command_input=input()
    if command_input=="3:1":
        break
    else:
        command_line=command_input.split()
        input_list=action[command_line[0]](int(command_line[1]),int(command_line[2]),input_list)
print(' '.join(input_list))