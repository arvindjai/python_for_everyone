# This program will print no of lines in file
count = 0
file = open('newfile.txt','r')
# print(file)
for text in file:
    # print(text)
    count += 1
    print(text.strip())
print("No of lines:", count)