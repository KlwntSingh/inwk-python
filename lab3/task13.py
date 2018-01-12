def abecedarian(word):
	last_chr=word[0]
	for chr in word[1:]:
		if ord(last_chr)>ord(chr):
			return False
		last_chr=chr
	return True


print(abecedarian("kulwant"))
print(abecedarian("abcedghij"))
