'''
Write a class that calculates and stores the height and weight of a person in metric. The file should be named lab.py. 
BMI is calculated using this formula:
Weight/Height^2 - weight is in kilograms and height is in meters.
The class should have two properties named:
    Weight
    Height
The class should have two methods:

    BMI_Value – This takes no arguments and returns a decimal value of the BMI
    Equals – This should override the equals method from the object class to compare the weight and height of two BMI objects.  
    To override the equal method you should implement this method: __eq__(self, other) and return a boolean
'''

class BMI:
    __pHeight = 0
    __pWeight = 0

    def __getHeight(self):
        return self.__pHeight
    def __setHeight(self,inValue):
        self.__pHeight = inValue
    height = property(__getHeight, __setHeight)

    def __getWeight(self):
        return self.__pWeight
    def __setWeight(self,inValue):
        self.__pWeight = inValue
    weight = property(__getWeight, __setWeight)

    def __eq__(self, other):
        return self.height == other.height and self.weight == other.weight
    

