fname = input("Enter file name: ")
fh = open(fname)
lst = list()
unique_word = []
for line in fh:
    word_list = line.rstrip().split()
    lst.extend(word_list)
    for word in lst:
        if word not in unique_word:
            unique_word.append(word)
unique_word.sort()
print(unique_word)