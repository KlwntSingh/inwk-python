def print_twice(s):
	print s

def do_twice(f, s):
	f(s)
	f(s)

def do_four(*p):
	do_twice(*p)
	do_twice(*p)

do_twice(print_twice, "kulwant")
do_four(print_twice, "kulwant")
