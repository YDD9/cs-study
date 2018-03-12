# http://www.geeksforgeeks.org/interpolation-search/

def interpolationSearch(arr, l, r, x):
    
    med = l + (x - arr[l])*(r - l)/(arr[r] - arr[l]) 

    if x == arr[med]:
        return med

    if x > arr[med]:
        return interpolationSearch(arr, med+1, r, x)
    
    if x < arr[med]:
        return interpolationSearch(arr, l, med-1, x)

def interpolationSearch2(arr, x):
    l = 0
    r = len(arr) - 1
    while l >= 0 and r < len(arr) and l <= r:
        med = l + (x - arr[l])*(r - l)/(arr[r] - arr[l]) 
        if x == arr[med]:
            return med
        if x > arr[med]:
            l = med + 1
        if x < arr[med]:
            r = med - 1
    return med




x = 5
arr = [2,4,5,6,8,10]
l = 0
r = len(arr) - 1

print interpolationSearch(arr, l, r, x)
print interpolationSearch2(arr, x)
