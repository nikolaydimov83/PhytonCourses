text=input()

for i in range(0,len(text)):
    if text[i]==':':
        print(f":{text[i+1]}")