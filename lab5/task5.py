import math
import matplotlib.pyplot as pt

log = math.log
def word_frequency(path):
    fileObj = open(path)
    word_count = {}
    for line in fileObj:
        line=line.strip()
        word_list = line.split()
        for word in word_list:
            if word in word_count:
                word_count[word]+=1
            else:
                word_count[word]=1

    word_list=list(word_count.keys())
    count_word={}
    for word in word_list:
        count=word_count[word]
        if count in count_word:
            count_word[count].append(word)
        else:
            count_word[count]=[word]

    count_list=list(count_word.keys())
    count_list.sort(reverse=True)
    max_x_value=max(count_list)

    pt.clf()
    pt.title("Ttiel")
    pt.xlabel("words")
    pt.ylabel("frequency")
    for index in range(len(count_list)):
        word = count_list[index]
        wordlist = count_word[count]

        for word in wordlist:
            #print(word, log(count), log(index+1))
            pt.plot(log(count), log(index+1))

    pt.show()


word_frequency("book.txt")