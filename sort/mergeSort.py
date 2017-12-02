# https://softwareengineering.stackexchange.com/questions/297160/why-is-mergesort-olog-n
# time O(nlog(n))
# space O(log(n))

def merge(l, left, median, right):
    l1 = l[left : median+1]
    l2 = l[median+1 : right+1]
    if not l1 or not l2:
        return l1 or l2
    i = j =  0
    # Keep in mind that k needs offset left as well
    k = left
    # move point k for list l if any of halves l1,l2 has a smaller value
    # then move point i/j of the corresponding half l1/l2 till one of the half is totally empty
    while i<len(l1) and j<len(l2):
        if l1[i] <= l2[j]:
            l[k] = l1[i]
            i += 1
        else:
            l[k] = l2[j]
            j += 1
        k += 1
    # update l with remaining elements in the non emptied half
    if i < len(l1):
        l[k : right+1] = l1[i :]
    if j < len(l2):
        l[k : right+1] = l2[j :]


def mergeSort(l, left, right):
    """
    original list l is updated continuously 
    so median calculation offset with left.

    mergeSort will first split list in two halves
    and split each half in two and repeat till signle element.

    then merge two single element
    then merge two sets of 2 elements
    and continue till the complete list
    """
    median = left + (right - left) // 2
    if left < right:
        mergeSort(l, left, median)
        mergeSort(l, median+1, right)
        merge(l, left, median, right)


# https://www.pythoncentral.io/merge-sort-implementation-guide/
# http://www.geeksforgeeks.org/merge-sort/

def mergeSort2(alist):
    print("Splitting ",alist)

    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        #recursion
        mergeSort2(lefthalf)
        mergeSort2(righthalf)

        i=0
        j=0
        k=0  # no offset because alist is input and it is updated everytime.

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

    print("Merging ",alist)

if __name__=='__main__':
    l = [4,1,5,2]
    mergeSort2(l)

    l = [2,4,1,5,6,3,8,7]
    mergeSort(l, 0, len(l)-1)
    print l