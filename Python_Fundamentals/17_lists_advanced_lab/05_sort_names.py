names_list=input().split(', ')
#sorted_list = sorted(names_list, key=lambda name:(-len(name), name))
sorted_list = sorted(names_list, key=lambda name: (len(name), name), reverse=True)
print(sorted_list)
