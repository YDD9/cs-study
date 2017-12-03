# http://www.geeksforgeeks.org/bubble-sort/

def bubbleSort(arr):
    swap = 0
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            arr[i] , arr[i+1] = arr[i+1], arr[i]
            swap += 1
    if not swap:
        return arr
    return bubbleSort(arr)

def bubbleSort2(arr):
    n = len(arr)
    for i in range(n):
        swap = 0
        # Last i elements are already in place
        # i==0, last element in arr will be found by bubblesort
        # i==1, last 2 elements in arr will be found by bubblesort
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap += 1
        if not swap:
            return arr



array = [7,9,4,3,6,1,12,15]
print bubbleSort(array)
print bubbleSort2(array)