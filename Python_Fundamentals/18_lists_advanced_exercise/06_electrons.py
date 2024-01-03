electrons_count=int(input())
electron_grid=[]

while(electrons_count>=(len(electron_grid)+1)**2*2):
    electrons_count-=(len(electron_grid)+1)**2*2
    electron_grid.append((len(electron_grid)+1)**2*2)
    

if electrons_count>0:
    electron_grid.append(electrons_count)
print(electron_grid)
