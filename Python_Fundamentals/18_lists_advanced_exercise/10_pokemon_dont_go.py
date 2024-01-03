distances_list=list(map(int, input().split(' ')))
total=0
def check_element(element, element_to_remove):
    if element>element_to_remove:
        return element-element_to_remove
    else:
        return element_to_remove+element
while len(distances_list)>0:
    index=int(input())
    if 0<=index<=len(distances_list)-1:
        element_to_remove=distances_list[index]
        total+=element_to_remove
        distances_list.pop(index)
        distances_list=list(map(lambda x:check_element(x,element_to_remove),distances_list))
    elif(index<0):
        element_to_remove=distances_list[0]
        total+=element_to_remove
        distances_list[0]=distances_list[len(distances_list)-1]
        distances_list=list(map(lambda x:check_element(x,element_to_remove),distances_list))
    elif (index>len(distances_list)-1):
        element_to_remove=distances_list[len(distances_list)-1]
        total+=element_to_remove
        distances_list[len(distances_list)-1]=distances_list[0]
        distances_list=list(map(lambda x:check_element(x,element_to_remove),distances_list))

print(total) 
