# Practice of  sorting, searching and basic programs

from collections import deque, Counter

#merge sort
def mergesort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]
        mergesort(left)
        mergesort(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1
            k+=1
        while i<len(left):
            arr[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            arr[k]=right[j]
            j+=1
            k+=1

def bubblesort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j+1],arr[j]=arr[j],arr[j+1]

def binarysearch(arr,val,low,high):
    if high>=low:
        mid=low+(high-low)//2
        if arr[mid]==val:
            return mid
        elif val<arr[mid]:
            return binarysearch(arr,val,low,mid-1)
        elif val>arr[mid]:
            return binarysearch(arr,val,mid+1,high)

def quicksort(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot=arr.pop()
    items_greater=[]
    items_lower=[]
    for item in arr:
        if item>pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
    return quicksort(items_lower)+[pivot]+quicksort(items_greater)


if __name__=='__main__':
    arr=[4,7,8,3,2,6,3,9,13]
    mergesort(arr)
    print(arr)
    arr = [4, 7, 8, 3, 2, 6, 3, 9, 13]
    bubblesort(arr)
    print(arr)
    n=len(arr)-1
    output=binarysearch(arr,6,0,n)
    print(output)
    arr = [4, 7, 8, 3, 2, 6, 3, 9, 13]
    arr=quicksort(arr)
    print(arr)

