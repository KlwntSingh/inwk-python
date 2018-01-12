def uses_all(word, requiredStr):
	for reqLetter in requiredStr:
		if reqLetter not in word:
			return False
	return True


print(uses_all("kulwant", "aeiou"))
print(uses_all("akueikdfjokerj", "aeiou"))
