fname = input("Enter file name:")
handle = open(fname)

counts = dict()
for line in handle:
    word_list = line.split()
    for word in word_list:
        counts[word] = counts.get(word, 0) + 1
print(counts)

big_count = None
big_word = None
for words, count in counts.items():
    if big_count is None or count > big_count:
        big_count = count
        big_word = words
print(big_word,big_count)
