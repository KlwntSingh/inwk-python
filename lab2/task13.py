def is_between(x,y,z):
	retVal=False
	if x < y and y < z:
		retVal=True
	return retVal


print(is_between(3,4,6))

