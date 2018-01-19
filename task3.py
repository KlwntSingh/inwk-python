def printer(n):
    for i in range(1, n+1):
        if i == 1:
            print(i)
        else:
            print(str(i)*(i))


printer(5)