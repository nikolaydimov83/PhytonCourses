initial_list=input().split()
removal_count=int(input())

for i in range(len(initial_list)):
    initial_list[i]=int(initial_list[i])

copy_list=initial_list.copy()
copy_list.sort()
reduced_list=copy_list[removal_count:]
final_list=[]
for i in initial_list:
    if i in reduced_list:
        final_list.append(str(i))
print(', '.join(final_list))