# http://www.geeksforgeeks.org/heap-sort/


def maxHeap(arr, n, maxIndex):
    """
    Max Heap: 
    check items in arr[: n] and identify the maximum among them
    Put the max item at the position maxIndex
    """
    l = 2 * maxIndex + 1
    r = 2 * maxIndex + 2
    larger = maxIndex
    if l < n and arr[maxIndex] < arr[l]:
        larger = l
    if r < n and arr[larger] < arr[r]:
        larger = r
    if larger != maxIndex:
        arr[maxIndex], arr[larger] = arr[larger], arr[maxIndex]
        maxHeap(arr, n, larger) # go deeper in the branch where node is swapped.
        
def heapSort(arr):
    totalN = len(arr)
    for i in range(totalN-1, -1, -1): # start from bottom leave to root build MaxHeap
        maxHeap(arr, totalN, i)
    for i in range(totalN-1, 0, -1) :
        arr[0], arr[i] = arr[i], arr[0]  # put max of i items at postion i
        maxHeap(arr, i, 0)  # exclude max of i items and keep heapify process
    return arr

l = [6, 5, 4, 3, 2, 1, 0]
l = [ 2,5,6,1,4,10,9,3,7,8]
l = [ 2, 1, 3, 5, 6, 7]
print heapSort(l)

