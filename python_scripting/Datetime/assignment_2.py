# write a program that reads in numbers until a -1 is entered and prints the sum of all 
# numbers entered in decimal format with two digits after the decimal.
# For example, if the user enters 5000 10 15 -1 the program should display 5025.00 
# (Each number will be separated by a carriage return).

sum = 0
x = int(input())
while x != -1:
    x = int(input())
    sum += x
print(f"Sum is: {sum:.2f}")