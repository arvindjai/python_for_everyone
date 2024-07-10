import re

with open('regex_sum_1949659.txt') as file:
    num_list = []
    for line in file:
        y = re.findall('[0-9]+',line) # Extracting numbers from everyline
        if y != []:                    # Check for non empty list
            for x in y: 
                int_x=int(x) 
                num_list.append(int_x)
    print(num_list)

    # Calculating Sum
    sum = 0
    for num in num_list:
        sum += num
    print(sum)