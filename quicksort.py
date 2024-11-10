def quickSort(arr):
    n = len(arr)
    if n<2:
        return arr
    pivot = arr[0]
    left = []
    right = []
    for i in range(1,n):
        if arr[i]<pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return quickSort(left) + [pivot] + quickSort(right)

if __name__=='__main__':
    from random import shuffle
    arr = list(range(10))
    shuffle(arr)
    print(arr)
    arr = quickSort(arr)
    print(arr)