team_a=[]
team_b=[]
suspended=False
comands=input().split(' ')

for i in range(len(comands)):
    intermediate=comands[i].split('-')
    if (intermediate[0]=='A'):
        if comands[i] not in team_a:
            team_a.append(comands[i])
            if len(team_a)>=5:
                suspended=True
                break
    else:
        if intermediate[0]:
            if comands[i] not in team_b:
                team_b.append(comands[i])
                if len(team_b)>=5:
                    suspended=True
                    break

print(f"Team A - {11-len(team_a)}; Team B - {11-len(team_b)}")
if suspended:
    print("Game was terminated")