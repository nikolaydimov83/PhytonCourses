class Zoo:
    __animals=0
    def __init__(self, name) -> None:
        self.name=name
        self.mammals=[]
        self.fishes=[]
        self.birds=[]
    
    def add_animal(self, species, name):
        if species=='mammal':
            self.mammals.append(name)
        if species=='fish':
            self.fishes.append(name)   
        if species=='bird':
            self.birds.append(name)       
        Zoo.__animals+=1

    def get_info(self, species:str):
        names=''
        species_string=''
        if species=='mammal':
            names=', '.join(self.mammals)
            species_string='Mammals'
        if species=='fish':
            names=', '.join(self.fishes)
            species_string='Fishes'   
        if species=='bird':
            names=', '.join(self.birds)
            species_string='Birds'
        

        return f"{species_string} in {self.name}: {names}\nTotal animals: {Zoo.__animals}"

zoo=Zoo(input())
itterations=int(input())

for i in range(itterations):
    command_line=input().split(' ')
    zoo.add_animal(command_line[0],command_line[1])
print(zoo.get_info(input()))
