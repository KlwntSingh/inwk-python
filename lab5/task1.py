import string

PUNCTUATIONS=string.punctuation

def conversion(path):
    fileObj = open(path)
    for line in fileObj:
        strippedLine=line.strip()
        wordList=strippedLine.split()
        for word in wordList:
            wd=word
            for ch in PUNCTUATIONS:
                wd=wd.replace(ch, "")
            print(wd.lower(), end=" ")
        print()

conversion("file.txt")

