# Count the Occurance of word in string and then store them in dictionary format.

def count(string):
    Dict = {}
    word = string.lower().split()
    # print(word)
    for key in word:
        Dict[key] = word.count(key)
    print(Dict)


string  = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb. Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go"
count(string)