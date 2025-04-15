class car:
    max_speed = 120
    def __init__(self,make,model,color,speed):
        "This method initializes instance attributes for make, model, color, and speed."
        self.make = make
        self.model = model
        self.color = color
        self.speed = speed
    def accelerate(self,acceleration):
        if self.speed + acceleration <= car.max_speed:
            self.speed += acceleration
        else:
            self.speed = car.max_speed
    def get_speed(self):
        return self.speed

car1 = car("toyota","Fortuner","blue",75)
car2 = car("dodge","challenger","white",40)

car1.accelerate(20)
print(f"{car1.make } {car1.model} is at speed of : {car1.speed}km/h having {car1.color} colour.")
