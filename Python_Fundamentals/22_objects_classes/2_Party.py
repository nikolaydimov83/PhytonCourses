class Party:
   
    def __init__(self) -> None:
        self.people=[]
        
    
    def command(self, command_input):
        
        if command_input!='End':
            self.people.append(command_input)
        else:
            print(f"Going: {', '.join(self.people)}")
            print(f"Total: {len(self.people)}")
party =Party()

while True:
    command_line=input()
    party.command(command_line)
    if command_line=='End':
        break
