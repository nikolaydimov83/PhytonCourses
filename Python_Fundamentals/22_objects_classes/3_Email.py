class Email:
    def __init__(self, sender, receiver, content, is_sent=False) -> None:
        self.sender=sender
        self.receiver=receiver
        self.content=content
        self.is_sent=is_sent
    def send(self):
        self.is_sent=True
    def  get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"
emails=[]    

while True:
    command=input()
    if command=='Stop':
        break
    else:
        splitted_command=command.split()
        emails.append(Email(splitted_command[0],splitted_command[1],splitted_command[2]))
indices=list(map(int,input().split(', ')))

for index in indices:
    emails[index].send()
for email in emails:
    print(email.get_info())