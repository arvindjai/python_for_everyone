f = open("demofile.txt")
# print(f.readline())  --> returns single line
# print(f.readlines())  --> returns list of all lines
for line in f:
    print(line.strip())  # Return all lines in file

w = open("demofile.txt", "a")
new_line = '''Love you too...'''
w.write(new_line)
w.close()