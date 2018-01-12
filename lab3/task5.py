def converser(word):
	length=len(word)
	if length < 3:
		return(word)
	else:
		last_three_words=word[-3:]
		if(last_three_words == "ing"):
			return word + "ly"
		else:
			return word+"ing"


print(converser("kulwant"))
print(converser("ing"))
print(converser("in"))
print(converser("kulwanting"))
