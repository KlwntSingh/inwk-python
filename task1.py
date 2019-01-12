sum=0


def sumOfElements(ls, index):
    global sum
    if index >= len(ls):
        return

    item=ls[index]
    if(isinstance(item, list)):
        sumOfElements(item, 0)
    else:
        sum+=item
        sumOfElements(ls, index+1)



ls=[1,2,3,4,5,[1,2,3,4,5, [1,2,3,4,5]]]

sumOfElements(ls, 0)
print(sum)