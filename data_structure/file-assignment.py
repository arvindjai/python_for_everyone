fn = input("Enter file name: ")
fh = open(fn)
count = avg = sum =  0
location = 0
for file in fh:
    file = file.rstrip()
    if file.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        file_loc = file.find(':')
        value = float(file[file_loc +1 :])
        sum = sum + value
avg = sum / count
print(avg)