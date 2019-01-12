from functools import reduce

def sum(a,b):
    if isinstance(b, list):
        return reduce(sum, [a, reduce(sum, b)])
    else:
        return a+b

def nested_sum(ls):
    sum = 0;
    for item in ls:
        if isinstance(item, list):
            sum+=nested_sum(item)
        else:
            sum+=item
    return sum

ls=[1,2,3,[1,2,3, [1,2,3]]]
print(nested_sum(ls))
print(reduce(sum, ls))