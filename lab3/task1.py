import sys
import math

epsilon=sys.float_info.epsilon

def square_root(a):
	x=2
	while True:
		y=(x+a/x)/2
		if abs(y-x)<epsilon:
			return(y)
		x=y

def math_square_root(a):
	return(math.sqrt(a))

def test_square_root(a):
	for num in range(1, a+1):
		custom_sqrt=square_root(num)
		math_sqrt=math_square_root(num)		
		diff_in_sqrt=abs(custom_sqrt-math_sqrt)
		print_table(num, custom_sqrt, math_sqrt, diff_in_sqrt)
		
def print_table(a,b,c,d):
	print("{:<20}    {:<20}    {:<20}    {}".format(a,b,c,d))

test_square_root(25)
