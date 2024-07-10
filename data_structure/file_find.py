file = open('mbox-short.txt')
for line in file:
    line = line.rstrip()
    if not line.startswith('From'):
        continue
    word = line.split()
    print(word[2])
print(type(word))