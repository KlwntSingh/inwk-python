def chrToAscii(a):
	return ord(a)

def asciiToChr(num):
	return chr(num)

firstCap='A'
lastCap='Z'
firstLow='a'
lastLow='z'

def Rot(word, n):
	firstCapCode=chrToAscii(firstCap)
	lastCapCode=chrToAscii(lastCap)
	firstLowCode=chrToAscii(firstLow)
	lastLowCode=chrToAscii(lastLow)
	for char in word:
		code=chrToAscii(char)
		if(code<=lastCapCode):
			rotateCode=firstCapCode
		elif(code<=lastLowCode):
			rotateCode=firstLowCode
		code-=rotateCode	
		code+=n
		code%=26
		print(asciiToChr(code+rotateCode))

Rot("KulwantS",25)
