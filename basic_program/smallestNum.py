smallest = None
for i in [5, 3 , 41, 23, 1, 74, 12, 23]:
    if smallest is None:
        smallest = i
    elif  i < smallest:
        smallest = i

print(smallest)
