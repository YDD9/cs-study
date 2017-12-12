# http://www.geeksforgeeks.org/quick-sort/

def quickSort(arr):
    l = 0
    r = len(arr) - 1
    return partition(arr, l, r)


def partition(arr, l, r):
    left = l
    right = r
    med = l + (r - l) // 2

    if l == r:
        return

    while l < r:
        if arr[l] > arr[med]:
            arr[l] , arr[med] = arr[med], arr[l]
        
        if arr[med] > arr[r]:
            arr[med], arr[r] = arr[r], arr[med]
        
        l += 1   
        r -= 1

    partition(arr, left, med-1)
    partition(arr, med+1, right)
    
    return arr


arr = [4,2,3,1,5,9,0]
r = len(arr) - 1
# print partition(arr, 0, r)
print quickSort(arr)