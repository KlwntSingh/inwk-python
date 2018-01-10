def is_triangle(a, b, c):
	if a + b >= c and b + c >= a and c + a >= b:
		print "Yes"
	else:
		print("No")


a=int(raw_input("First side: "))
b=int(raw_input("Second side: "))
c=int(raw_input("Third side: "))

is_triangle(a, b, c)
