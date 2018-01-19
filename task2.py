def gcd(a, b, c):
    minNumber = min(a, b, c)
    if minNumber == a:
        otherNumber1 = b
        otherNumber2 = c
    elif minNumber == b:
        otherNumber1 = a
        otherNumber2 = c
    else:
        otherNumber1 = a
        otherNumber2 = b

    gcdn = 1
    for i in range(1, minNumber):
        if otherNumber1 % i ==0 and otherNumber2 % i == 0:
            gcd=i

    return gcd

print(gcd(2, 3, 4))


def gcd_reduce_fn(a, b):

    div, num1, num2 = b
    if num1 % div == 0 and num2 % div == 0:
        return div
    else:
        return a

from functools import reduce

def gcd_with_reduce(a, b, c):
    if a < b and a < c:
        minNumber = a
        otherNum1 = b
        otherNum2 = c
    elif b < a and b < c:
        minNumber = b
        otherNum1 = a
        otherNum2 = c
    else:
        minNumber = c
        otherNum1 = b
        otherNum2 = a


    ls=list(range(1, minNumber))
    return reduce(gcd_reduce_fn, ls)

print(gcd_with_reduce(2, 3, 4))