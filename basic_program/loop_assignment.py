smallest = None
largest = None
num_list = []
while True:
    user_input = input("Enter number:")
    if user_input == 'done':
        break
    try:
        num = int(user_input)
        num_list.append(user_input)
    except:
        print("Invalid input")

print(num_list)

# Converting string list to integer list
int_num = [int(i) for i in num_list]
print(int_num)

# Finding Smallest
for x in int_num:
    if smallest is None:
        smallest = x
    elif x < smallest:
        smallest = x
print(smallest)

# Finding Largest
for y in int_num:
    if largest is None:
        largest = y
    elif y > largest:
        largest = y
print(largest)

        