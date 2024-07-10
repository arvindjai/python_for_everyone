count = dict()
line = 'It is the east and Juliet is the sun'
word_list = line.split()
for word in word_list:
    count[word] = count.get(word, 0) + 1
print(count)
