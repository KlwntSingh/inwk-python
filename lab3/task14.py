def puzzler(word):
	for i in range(len(word)):
		double_letters_count=0
		j = i
		while j in range(len(word[:])-1):
			if word[j] == word[j+1]:
				double_letters_count+=1
			else:
				double_letters_count=0
			if double_letters_count == 3:
				return True
			j+=2
	return False

print(puzzler("mississippi"))
print(puzzler("aaabbcc"))
print(puzzler("aaabbbcc"))
print(puzzler("aaabbccc"))
print(puzzler("baaabbccc"))

