ls=[1,2,3,4,5,[1,2,3,4,5, [1,2,3,4,5]]]

def looping():
    sum=0
    index=0
    internalIndex=0
    length=len(ls)
    while index<length:
        item=ls[index]
        if(isinstance(item, list)):
            if internalIndex == 0:
                #length+=len(item)
                internalIndex=len(item)

            sum+=item[internalIndex-1]

            internalIndex-=1
            if internalIndex == 0:
                index+=1

        else:
            sum+=item
            index+=1

    return sum
print(looping())
#print(sum)