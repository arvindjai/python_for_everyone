numlist = list()

while True:
    inp = input("Enter number:")
    if inp == 'done':
        break
    num = int(inp)
    numlist.append(num)
average = sum(numlist) / len(numlist)
print(average)