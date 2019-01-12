from task1 import *


def word_counter(*paths):
    books = {}
    for path in paths:
        word_count_dict = {}
        total_word_count = 0

        fileObj = open(path)
        for line in fileObj:
            stripped_line=line.strip()
            word_list=stripped_line.split()
            for word in word_list:
                wd = word
                for ch in PUNCTUATIONS:
                    wd = wd.replace(ch, "")

                if wd in word_count_dict:
                    word_count_dict[wd] += 1
                else:
                    word_count_dict[wd] = 1
                total_word_count += 1

        different_words_list = word_count_dict.keys()
        count_to_word_dict = {}

        for word in different_words_list:
            count = word_count_dict[word]
            if count in count_to_word_dict:
                count_to_word_dict[count].append(word)
            else:
                count_to_word_dict[count] = [word]

        word_count_list = list(count_to_word_dict.keys())
        word_count_list.sort(reverse=True)

        number_to_print=20

        most_frequently_used_words = []
        for word_count_in_list in word_count_list:
            ls = count_to_word_dict[word_count_in_list]
            index = 0
            while number_to_print >= 0 and index < len(ls):
                    most_frequently_used_words.append(ls[index])
                    index += 1
                    number_to_print -= 1

            if number_to_print < 0:
                break
        books[path] = total_word_count, word_count_dict, different_words_list, most_frequently_used_words

    return books

filePath = "book.txt"
filePath2 = "book1.txt"

# conversion(filePath)
print(word_counter(filePath))


