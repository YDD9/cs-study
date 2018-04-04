# http://www.geeksforgeeks.org/quick-sort/

def quickSort(arr, le, ri):
    if le < ri:
        m = partition(arr, le, ri)
        quickSort(arr, le, m)
        quickSort(arr, m+1, ri)
    return arr


def partition(arr, l, r):
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

    return med


# arr = [4,2,3,1,5,9,0]
arr = [5,2,4,3,6]
# arr = [5,4,3,2,1]
ri = len(arr) - 1
print quickSort(arr, 0, ri)