# http://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array-set-2-expected-linear-time/
# kth order statistic: Quickselect
# https://en.wikipedia.org/wiki/Quickselect
# https://www.quora.com/What-is-the-most-efficient-algorithm-to-find-the-kth-smallest-element-in-an-array-having-n-unordered-elements

# http://www.geeksforgeeks.org/find-k-th-smallest-element-in-bst-order-statistics-in-bst/
# http://www.geeksforgeeks.org/k-largestor-smallest-elements-in-an-array/

# import random
# def kthSmall(arr, k, flag='small'):
#     l = 0
#     r = len(arr) - 1
#     med = random.randint(l, r)
#     med = 3

#     def partition(arr, l, r):

#         while l <= r:
#             if l == r:
#                 return
#             if arr[l] > arr[med]:
#                 arr[l], arr[med] = arr[med], arr[l]
#             if arr[med] > arr[r]:
#                 arr[med], arr[r] = arr[r], arr[med]
#             l += 1
#             r -= 1

#     partition(arr, l, med, r)
#     # if med == k:
#     #     print arr[k]        
#     #     return arr[k]
#     if med < k:
#         partition(arr, med+1, k, r)
#     if med > k:
#         partition(arr, l, k, med-1) 
#     print arr[k]
#     return arr[k]

# arr = [2,4,5,8,1,3]
# kthSmall(arr, 5)


# Python program for implementation of Quicksort Sort
 
# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partition(arr,low,high):
    i = ( low-1 )         # index of smaller element
    pivot = arr[high]     # pivot
 
    for j in range(low , high):
 
        # If current element is smaller than or
        # equal to pivot
        if   arr[j] <= pivot:
         
            # increment index of smaller element
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
 
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )
 
# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index
 
# Function to do Quick sort
def quickSort(arr,low,high):
    if low < high:
 
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr,low,high)
 
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
 
# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i]),
 
# This code is contributed by Mohit Kumra
