handle = open('romeo.txt')
counts = dict()
for line in handle:
    word_list = line.split()
    for word in word_list:
        counts[word] = counts.get(word,0) + 1
lst = []
for k,v in counts.items():
    temp_tuple = (v,k)
    lst.append(temp_tuple)

lst = sorted(lst, reverse=True)
# print(lst)
for v,k in lst[:10]:
    print(k,v)
        
