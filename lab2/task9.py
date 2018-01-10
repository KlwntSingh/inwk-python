def do_n(f, n):
	for i in range(n):
		f()

def test():
	print "called"

do_n(test, 10)
