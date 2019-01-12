from functools import reduce

def check_even(num):
    if num%2==0:
        return True

def square(num):
    return num**2

def sum(a,b):
    return a+b

ls=[1,2,3,4,5,6]
print(reduce(sum, map( square, filter(check_even, ls))))