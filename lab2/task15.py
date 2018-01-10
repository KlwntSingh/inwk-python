def first(word):
	return word[0:1]

def last(word):
	return word[-1:]

def middle(word):
	return word[1:-1]

print(middle(''))
print(middle('kk'))
print(middle('ku'))


def is_palindrome(word):
	if word:
		if (first(word) == last(word)) and is_palindrome(middle(word)):
			return True
		else:
			return False
	else:
		return True


print(is_palindrome('kulwant'))
print(is_palindrome('redivider'))
print(is_palindrome('noon'))
