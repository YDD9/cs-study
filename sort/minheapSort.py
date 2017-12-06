def minHeap(arr, n, minId):
    l = 2 * minId + 1
    r = 2 * minId + 2
    smaller = minId
    if l < n and arr[l] < arr[minId]:
        smaller = l
    if r < n and arr[r] < arr[smaller]:
        smaller = r
    if smaller != minId:
        arr[minId], arr[smaller] = arr[smaller], arr[minId]
        minHeap(arr, n, smaller)

def minHeapSort(arr):
    n = len(arr)
    ascResult = [None]*n
    for i in range(n-1, -1, -1):
        minHeap(arr, n, i)
    for j in range(n-1, 0, -1):
        ascResult[n-1-j] = arr[0]
        arr[0], arr[j] = arr[j], arr[0]
        minHeap(arr, j, 0)
    ascResult[n-1] = arr[0]
    print ascResult  # ascResult = arr[::-1]
    return arr 

l = [0,5,2,3,4,1]
l = [5]
l = [5,4,3,2]
l = [1,2,3,4,5]
print minHeapSort(l)[::-1]
