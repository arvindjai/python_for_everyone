class vehicle:
    color = "white"
    def __init__(self,max_speed, milage):
        self.max_speed = max_speed
        self.milage = milage
        self.seat = None
    def seating_capacity(self,seat):
        self.seat = seat
    def display_properties(self):
        print("Displaying properties of Vehicles")
        print(f"color: {self.color}")
        print(f"Max speed: {self.max_speed} kmph")
        print(f"Milage: {self.milage}kmph")
        print(f"seating capacity: {self.seat}")
car1 = vehicle(200,20)
car1.seating_capacity(5)

car2 = vehicle(180,25)
car2.seating_capacity(4)

car1.display_properties()
car2.display_properties()