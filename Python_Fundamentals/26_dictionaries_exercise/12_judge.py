dictionary={}
submissions={}

while True:
    command_line=input()
    if command_line=="exam finished":
        break
    if command_line.find('banned')>-1:
        name, banned=command_line.split('-')
        for language, users in dictionary.items():
            if name in users:
                users[name][banned]=True
    else:
        name, language, points=command_line.split('-')
        points=int(points)
        if language not in dictionary:
            dictionary[language]={}
            submissions[language]=0
        if name not in dictionary[language]:
            dictionary[language][name]={"banned":False}
        try: 
            dictionary[language][name]["points"]=max(points,dictionary[language][name]["points"])
            submissions[language]+=1
        except:
            dictionary[language][name]["points"]=points
            submissions[language]+=1
print("Results:")

for language, user in dictionary.items():
    for username, values in user.items():
        if values["banned"]==False:
            print(f"{username} | {values['points']}")


print("Submissions:")
for language, val in submissions.items():
    print(f"{language} - {val}")