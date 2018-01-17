def findBiggestInOrder(a, b, c, d):
    if a > b:
        if b > c:
            if c > d:
                return (a,b,c,d)
            else:
                return (a,b,d,c)
        else:
            if b > d:
                return (a,c, b, d)
            else:
                return (a, c, d, b)
    else:
        if a > c:
            if c > d:
                return (b, a ,c,d)
            else:
                return (b, a,c, d)
        else:
            if a > d:
                return (b, c, a, d)
            else:
                return (b, c, d, a)

a=int(input("First number"))
b=int(input("Second number"))
c=int(input("Third number"))
d=int(input("Fourth number"))
(a, b, c, d)=findBiggestInOrder(a, b, c ,d)
print("largest number", a)
print("second largest number", b)
print("third largest number", c)
