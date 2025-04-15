class PartyAnimal:
    def __init__(self,nam):
        self.x = 0
        self.name = nam
    def party(self):
        self.x = self.x + 1
        print("So far", self.x)


class FootballFan(PartyAnimal): # Football is class which extends PartyAnimal
    def __init__(self, nam):
        super().__init__(nam)
        self.points = 0
    
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, "points", self.points)
    

s = PartyAnimal("Sally")
s.party()
s.party()

j = FootballFan("Jim")
j.party()
j.touchdown()
