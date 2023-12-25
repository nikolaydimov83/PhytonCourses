firstString=input()
secondString=input()

length=len(firstString)

for i in range(length):
    if firstString[i]==secondString[i]:
        continue
    else:
        firstString= firstString[:i] + secondString[i] + firstString[i+1:]
        print(firstString)
