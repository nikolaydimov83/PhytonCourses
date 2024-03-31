text=input()

def abjuration(command):
    global text
    text=text.upper()
    print(text)
def necromancy(command):
    global text
    text= text.lower()
    print(text)

def illusion(command):
    global text
    splitted=command.split(" ")
    index1=int(splitted[1])
    letter=splitted[2]
    if index1>len(text)-1:
        print("The spell was too weak.")
    else:
        print("Done!")
        text = text[:index1] + letter + text[index1+ 1:]
        

def divination(command):
    global text
    splitted=command.split(" ")
    substring1=splitted[1]
    substring2=splitted[2]
    if text.count(substring1)>0:
        text = text.replace(substring1, substring2)
        print(text)
def alteration(command):
    global text
    splitted=command.split(" ")
    substring1=splitted[1]
    if text.count(substring1)>0:
        text = text.replace(substring1, "")
        print(text)
    else:
        print("The spell did not work!")
action={"Abjuration": abjuration, "Necromancy":necromancy,"Illusion":illusion,"Divination":divination, "Alteration":alteration}
while (True):
    command = input()
    if command=="Abracadabra":
        break
    index=command.split()[0]
    if index not in ["Abjuration", "Necromancy","Illusion","Divination", "Alteration"]:
        print("The spell did not work!")
        continue
    action[index](command)
    
    
