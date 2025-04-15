f = open("indata.txt", "r")
sum = 0.00
for line in f:
    sum += float(line)
print("{0:3.2f}".format(sum))