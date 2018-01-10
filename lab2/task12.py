import turtle

def fd(t, length):
	t.fd(length)
def lt(t, angle):
	t.lt(angle)
def rt(t, length):
	t.rt(length)
def bk(t, length):
	t.bk(length)

def draw(t, length, n):
	if n == 0:
		return
	angle=50
	fd(t, length*n)
	lt(t, angle)
	draw(t, length, n-1)
	rt(t, 2*angle)
	draw(t, length, n-1)
	lt(t, angle)
	bk(t, length*n)

bob=turtle.Turtle()

def koch(length):
	if length < 3:
		bob.fd(length)
		return

	draw(bob, length/3, 4)
	bob.lt(60)
	draw(bob, length/3, 4)
	bob.rt(120)
	draw(bob, length/3, 4)
	bob.lt(60)
	draw(bob, length/3, 4)

koch(30)

turtle.mainloop()
