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


def koch(t, length):
	if length < 3:
		t.fd(length)
		return
	sides=5
	koch(t, length/3)
	t.lt(60)
	koch(t, length/3)
	t.rt(120)
	koch(t, length/3)
	t.lt(60)
	koch(t, length/3)

def snowflake(t, length):
	for i in range(3):
		koch(t, length)
		t.rt(120)


bob=turtle.Turtle()
koch(bob, 40)

turtle.mainloop()
