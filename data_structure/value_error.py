import math
def function1(num):
    square_root = math.sqrt(num)
    return square_root

try:
    number1 = float(input("Enter Positive number: "))
    print(function1(number1))
except ValueError or number1 < 0:
    print("Invalid input! Please enter a positive integer or a float value.")
