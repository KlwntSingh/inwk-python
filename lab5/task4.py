def word_list_to_dict(pathToWordList):
    word_dict = set()
    word_list_obj = open(pathToWordList)

    for word in word_list_obj:
        word = word.strip()
        word_dict.add(word)

    return word_dict


def word_checker_in_list(pathToBook, pathToWordList):
    book_obj = open(pathToBook)
    word_dict = word_list_to_dict(pathToWordList)
    
    for line in book_obj:
        stripped_line = line.strip()
        line_array = stripped_line.split()
        for word in line_array:
            if word not in word_dict:
                print(word)


path1 = "book.txt"
path2 = "words.txt"
word_checker_in_list(path1, path2)