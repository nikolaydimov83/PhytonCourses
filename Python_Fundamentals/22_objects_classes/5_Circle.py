class Circle:
    __pi=3.14
    def __init__(self,diameter) -> None:
        self.diameter=diameter
    
    def  calculate_circumference(self):
        return self.diameter*Circle.__pi
    
    def calculate_area(self):
        return (self.diameter/2)**2*Circle.__pi
    def calculate_area_of_sector(self, angle):
        return (self.diameter/2)**2*Circle.__pi*angle/360