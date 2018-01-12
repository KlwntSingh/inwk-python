def avoids(word, forbiddenStr):
	for letter in word:
		if letter in forbiddenStr:
			return False
	return True

print(avoids("kulwant", "singh"))
print(avoids("kulwant", "ved"))
