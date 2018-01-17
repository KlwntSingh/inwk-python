finalResult=[]
def listTraversal(ls):
    for index in range(len(ls)):
        i=ls[index]
        if isinstance(i, list):
            return listTraversal(i)
        else:
            finalResult.append((index, type(i)))

listTraversal([1,2,3,['kulwant', 'singh']])
print(finalResult)
