fname = input("Enter file name: ")
with open(fname) as file:
    file_context = file.read()

    word_list = file_context.split()
    # print(word_list)
    sorted_word = []

    for word in word_list:
        sorted_word.append(word)
    sorted_word.sort()
    print(sorted_word)