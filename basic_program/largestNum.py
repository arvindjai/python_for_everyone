# list_num = [5, 3 , 41, 23, 1, 74, 12, 23]

largest = None
for i in [5, 3 , 41, 23, 1, 74, 12, 23]:
    if largest is None:
        largest = i
    elif i > largest:
        largest = i
    
print(largest)