# Input
# heapArr: heap array [1..n] where heapArr[1] is root, 
#                                  heapArr[2*index] is left subtree,
#                                  heapArr[2*index+1] is right subtree
# index: index of item to be sifted down (from root (index 1))
def siftdown(heapArr:list, index:int):
    n = len(heapArr)
    largest = index
    leftIndex = 2*index 
    rightIndex = 2*index + 1

    if leftIndex <= n and heapArr[leftIndex-1] > heapArr[largest-1]:
        largest = leftIndex
    if rightIndex <= n and heapArr[rightIndex-1] > heapArr[largest-1]:
        largest = rightIndex

    if largest != index:
        heapArr[index-1], heapArr[largest-1] = heapArr[largest-1], heapArr[index-1] # Swap index and largest
        siftdown(heapArr, largest)

# Input: Array of int [1...n]
# Output: Max Heap Array of int [1...n], where arr[1] is the largest int
def heapify(arr):
    n = len(arr)
    for i in range(n//2,0,-1):
        siftdown(arr,i)
    return arr

def heapSort(arr):
    n = len(arr)
    heapify(arr)
    for i in range(n-1,0,-1):
        arr[i], arr[0] = arr[0], arr[i]
        heap = arr[:i]
        siftdown(heap, 1)
        arr[:i] = heap
    return arr

if __name__=='__main__':
    from random import shuffle
    arr = list(range(100))
    shuffle(arr)
    arr = arr[:7]
    print(arr)
    print(heapSort(arr))