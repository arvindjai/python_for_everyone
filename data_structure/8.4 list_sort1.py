fname = input("Enter file name: ")


lst = list()
fh = open(fname, 'r')
for line in fh:
    word_list = line.rstrip().split()
    for word in word_list:
        if word not in lst:
            lst.append(word)
fh.close()

lst.sort()
print(lst)