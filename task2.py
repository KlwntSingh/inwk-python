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