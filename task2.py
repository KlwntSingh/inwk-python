import functools
from functools import reduce

#print(dir(functools))

def check_even(num):
    if num % 2 == 0:
        return True

def sum(a,b):
    return a+b

ls=list(range(100, 500))
print(reduce(sum, filter(check_even, ls)))



def capitalizer(item):
    return item.capitalize()

ls="kulwant singh"


#print(dir(map))
print(list(map(capitalizer, ls)))