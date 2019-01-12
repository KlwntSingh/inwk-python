from functools import reduce

def commulative_sum(list, a):
    if isinstance(list, int):
        return [list, list+a]
    list.append(list[len(list) - 1] + a)
    return list
ls=[1,2,3,4,4]
print(reduce(commulative_sum,ls))