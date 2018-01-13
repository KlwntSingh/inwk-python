def fibo(n, start):
    a=0
    for i in range(n):
        if i == 0:
            printFib(i, i, start)
            b = 1
        else:
            printFib(b, i, start)
            a,b = b,a+b


def printFib(num, i, start):
    if i >= start:
        print(num)



fibo(8,5)