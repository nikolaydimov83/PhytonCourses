
import math
prod1=int(input())
prod2=int(input())
prod3=int(input())
remaining_students=int(input())
hours_played=0
total_prod=prod1+prod2+prod3
while remaining_students>0:
    if ((hours_played+1)%4==0):
        hours_played+=1
        continue
    
    else:
        remaining_students-=total_prod
        hours_played+=1



print(f"Time needed: {hours_played}h.")