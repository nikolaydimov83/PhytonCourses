companies={}

while True:
    command__line=input().split(' -> ')
    if command__line[0]=='End':
        break
    if command__line[0] in companies:
        if command__line[1] not in companies[command__line[0]]:
            companies[command__line[0]].append(command__line[1])
    else:
        companies[command__line[0]]=[command__line[1]]

for company, employyes in companies.items():
    print(f"{company}")
    for employee in employyes:
        print(f"-- {employee}")