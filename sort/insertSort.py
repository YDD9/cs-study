# http://www.geeksforgeeks.org/insertion-sort/

def insertSort(arr):
    n = len(arr)
    for selectIndex in range(1, n):
        for j in range(selectIndex-1, -1, -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

array = [7,5,3,9,6,8]
print insertSort(array)

# http://www.geeksforgeeks.org/recursive-insertion-sort/
def insertSort2(arr, insertIndex):
    if insertIndex == len(arr):
        return arr
    for j in range(insertIndex-1, -1, -1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
    return insertSort2(arr, insertIndex+1)

print insertSort2(array, 1)