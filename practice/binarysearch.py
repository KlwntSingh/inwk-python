def binary_search(arr, item):
    lenth = len(arr)
    if lenth == 0:
        return -1
    midIndex = int(lenth/2)
    midItem = arr[midIndex]
    if( item > midItem ):
        return binary_search(arr[midIndex:], item) + midIndex
    elif (item < midItem):
        return binary_search(arr[:midIndex], item)
    else:
        return lenth/2


print(binary_search([1,2,3,5,6,7,8],3))