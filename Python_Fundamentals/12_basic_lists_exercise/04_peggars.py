revenues=input().split(', ')
beggars_count=int(input())
beggars_info=[]

for i in range((beggars_count)):
    beggars_info.append(0)

while len(revenues)>0:
    for i in range((beggars_count)):
        if len(revenues)==0:
            break
        beggars_info[i]+=int(revenues[0])
        revenues.pop(0)
print(beggars_info)
