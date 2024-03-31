array_targets=[int(i) for i in input().split(' ')]
shot_targets=0

while True:
    user_input=input()
    if user_input=='End':
        break
    index=int(user_input)
    if index>=0 and index<len(array_targets):
        
        target=array_targets[index]
        
        if target>-1:
            array_targets[index]=-1
            shot_targets+=1
            for i in range(len(array_targets)):
                if i==index or array_targets[i]==-1:
                    continue

                if array_targets[i]>target:
                    array_targets[i]=array_targets[i]-target
                else:
                    array_targets[i]=array_targets[i]+target

print(f"Shot targets: {shot_targets} -> {' '.join(list(map(str,array_targets)))}")
