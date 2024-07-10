# Creating an instance of a class: circle
class circle(object):
    def __init__(self,radius,colour):
        self.radius = radius
        self.colour = colour
        print("Radius of circle : ",self.radius)
        print("Colour of circle : ",self.colour)

c1 = circle(10, 'red') # c1:Object name; circle: className

c2 = circle(5,'blue')
# c2.colour = 'Orange'