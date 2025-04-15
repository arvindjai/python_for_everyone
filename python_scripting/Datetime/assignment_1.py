# Write a program that reads in a number and prints the date 
# that number of days from now in this format: Saturday, February 06, 2021.


from datetime import datetime
from datetime import timedelta

y = int(input())
x = datetime.now() + timedelta(days=y)
print(x.strftime("%A, %B %d, %Y"))


# Alternatives

# import datetime

# days = int(input("Enter number of day."))
# today = datetime.date.today()

# future_date = today + datetime.date.resolution * days

# formatted_date = future_date.strftime("%A, %B %d, %y")
# print(formatted_date)

