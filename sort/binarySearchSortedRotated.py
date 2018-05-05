# no recursive, binarySearch for both sorted and sorted rotation
# https://articles.leetcode.com/searching-element-in-rotated-array/#comment-1313
def bestBinarySearch(arr, x):
    l = 0
    r = len(arr) - 1

    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        # left part is sorted
        if arr[l] <= arr[mid]:
            if arr[l] <= x < arr[mid]:
                r = mid - 1
            else:
                l = mid + 1
        # if arr[mid] <= arr[r]:
        # right part is sorted
        else:
            if arr[mid] < x <= arr[r]:
                l = mid + 1
            else:
                r = mid - 1


def getPivotIndex(arr, l, r):
    if arr[l] < arr[r]: return -1
    mid = l + (r -l) // 2
    if arr[mid] > arr[mid+1]: return mid+1
    if arr[l] <= arr[mid]:
        return getPivotIndex(arr, mid+1, r )
    else:
        return getPivotIndex(arr, l, mid)


# target = 22
# sortRotatedArr = [44, 0, 11, 22, 33]
# l = 0
# r = len(sortRotatedArr)-1
# pivotIndex = getPivotIndex(sortRotatedArr, l, r)
# print '{} \nPivot point {} is at position\
#  {}'.format(sortRotatedArr,sortRotatedArr[pivotIndex],pivotIndex)


# print bestBinarySearch([44, 55, 11, 22, 33], 33)
print bestBinarySearch([4, 5, 1, 2, 3], 5)