import math

PI=math.pi

def square(side):
    return side**2

def circle(radius):
    return PI * radius**2

def sphere(radius):
    return 4*PI*radius**2


radius=int(input("Enter the length of side"))

print(square(radius))
print(circle(radius))
print(sphere(radius))

