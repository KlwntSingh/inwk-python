
def right_justify(s):
	length = len(s)
	space_length=70-length
	for i in range((space_length)):
		print "",
	print s

right_justify("singh")
