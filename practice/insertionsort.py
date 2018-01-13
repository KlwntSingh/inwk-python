def insertion_sort(arr):
    length = len(arr)
    for i in range(length):
        num = arr[i]
        for j in range(len(arr[:i])):
            if num < arr[j]:
                arr=arr[:j] + [num] + arr[j:i] + arr[i+1:]
                break
    print(arr)


insertion_sort([9,3,4,2,9,5,4,3])