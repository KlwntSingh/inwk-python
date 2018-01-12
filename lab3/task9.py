def printEachWordIfGreaterThanLength(filePath, mode, length):
	flObj=open(filePath, mode)
	for word in flObj:
		word=word.strip()
		if len(word) > length:
			print(word)


printEachWordIfGreaterThanLength("words.txt", "r", 20)
