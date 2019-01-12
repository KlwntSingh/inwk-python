def printer(n):
    old = 0
    for i in range(1, n+1):
        new = old * 10 + 1
        print(new*i)
        old=new

printer(5)