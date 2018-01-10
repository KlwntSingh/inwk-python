import turtle
import math

pi=math.pi

def polygon(b, numOfSides, length, angle):
	for i in range(numOfSides):
		b.fd(length)
		b.lt(angle)

def circle(b, radius, arc):
	circumference=2*pi*radius

	numOfSides = 100
	length = int(circumference/numOfSides)
	
	angle=360/numOfSides
	numOfSides=arc/angle
	for i in range(numOfSides+1):
		b.fd(length)
		b.lt(angle)


def square(b, length, angle):
	for i in range(4):
		b.fd(length)
		b.lt(angle)


bob=turtle.Turtle()
#polygon(bob, 10, 50, 45)

circle(bob, 50, 90)
turtle.mainloop()





