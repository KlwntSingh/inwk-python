def check_fermat(a, b, c, n):
	if n <= 2:
		print "give n greater than 2"
		return

	leftSide=a**n + b**n
	rightSide=c**n
	
	if a > 0 and b > 0 and c > 0 and leftSide != rightSide:
		print("No, that doesn't work")
	else:
		print("Holy smokes, Fermat was wrong!")


a=int(raw_input("First number i.e a "))
b=int(raw_input("Second number i.e b "))
c=int(raw_input("third number i.e c "))
n=int(raw_input("n "))

check_fermat(a,b,c,n)

