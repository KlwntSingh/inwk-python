def selection_sort(arr):
    length=len(arr)
    for i in range(length):
        min = arr[i]
        index=i
        for j in range(i, length):
            num=arr[j]
            if num < min:
                min=num
                index=j
        arr[i],arr[index]=min,arr[i]
    print(arr)

arr=[7,3,6,4,2,4,5,6,8,8,5]
selection_sort(arr)
