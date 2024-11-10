# Input: 2 sorted arrays (Left, Right) of nearly equal length
# Output: 1 sorted array
def merge(L, R):
    result = [] # Resulting array
    i = 0 # Left index
    j = 0 # Right index
    while (i < len(L) and j < len(R)):
        if L[i] < R[j]:
            result.append(L[i]) #Item i of left arr smaller than item j of right arr
            i += 1
        else:
            result.append(R[j]) #Item i of left arr greater than or equal to item j of right arr
            j += 1
    return result + L[i:] + R[j:]

def mergeSort(arr):
    n = len(arr)
    if n==1:
        return arr
    return merge(mergeSort(arr[:n//2]),mergeSort(arr[n//2:]))

if __name__=="__main__":
    print(merge([1,4,7,9,10],[3,5,8,11])) #Testing merge function
    print()
    from random import shuffle
    arr = list(range(100))
    shuffle(arr)
    arr = arr[:10]
    print(arr)
    print(mergeSort(arr))
    
    