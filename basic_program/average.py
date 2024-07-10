count = 0
sum = 0
for i in [5, 3 , 41, 23, 1, 74, 12, 23]:
    count = count + 1
    sum = sum + i
    print(count, i)
print("Total elements:",count)
print("Sum of all values:", sum)
avg = sum / count
print("Average:" , avg)