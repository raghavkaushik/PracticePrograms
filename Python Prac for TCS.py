# Practice of  sorting, searching and basic programs
import collections
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

def asteriodcollision(arr):
    result=[]
    for i in range(len(arr)):
        if arr[i]<0  and len(result)>0 and result[-1]>0:
            if abs(arr[i])==result[-1]:
                result.pop(-1)
                break
            elif abs(arr[i])<result[-1]:
                break
            else:
                result.pop(-1)
                continue
        else:
            result.append(arr[i])
    return result

def maxinslidingwindow(arr):
    result=[]
    queue=deque()
    l=r=0
    k=3
    while(r<len(arr)):
        while(queue and arr[queue[-1]]<arr[r]):
            queue.pop()
        queue.append(r)
        if l>queue[0]:
            queue.popleft()
        if r+l>=k:
            result.append(arr[queue[0]])
            l+=1
        r+=1
    return result

def rainwater(arr):
    leftmax=0
    rightmax=0
    low=0
    result=0
    high=len(arr)
    while(low<=high):
        if arr[low]<arr[high]:
            if leftmax<arr[low]:
                leftmax=arr[low]
            else:
                result+=leftmax-arr[low]
            low+=1
        else:
            if rightmax<arr[high]:
                rightmax=arr[high]
            else:
                result+=rightmax-arr[high]
            high-=1
    return result

def equalbrackets(arr):
    queue=[]
    flag=0
    for i in arr:
        if i in ['[','(','{']:
            queue.append(i)
        else:
            if not queue:
                flag+=1
            j=queue.pop()
            if j=='(':
                if i!=')':
                    flag+=1
            if j == '[':
                if i != ']':
                    flag += 1
            if j == '{':
                if i != '}':
                    flag += 1
    if queue:
        flag+=1
    if flag==0:
        return "matching"

def palindromestring(st):
    lst=(i for i in st)
    counter=Counter(lst)
    stack=[]
    for key,value in counter.items():
        if value%2==0:
            stack.append(key)
            lst.remove(key)
    lst.append(stack[0])
    print("minimum number of chars to be removed is:", len(stack) - 1)

def maxsubarraysum(arr):
    maximum=maxarray=arr[0]
    for i in range(1,len(arr)):
        maxarray=max(arr[i],maxarray+arr[i])
        maximum=max(maximum,maxarray)
    print(maximum)

def nextgreatestelement(arr):
    dt={}
    queue=[]
    queue.append(arr.pop(0))
    for i in range(len(arr)):
        if len(queue)==0:
            queue.append(arr.pop(0))
            continue
        while (queue and queue[-1]<arr[i]):
            dt[queue.pop(-1)]=arr[i]
        queue.append(arr[i])
    print(dt)
    print(queue)

def longestincseq(arr):
    lis=[1]*len(arr)
    for i in range(len(arr)-1,-1,-1):
        for j in range(i+1,len(arr)):
            if arr[i]<arr[j]:
                lis[i]=max(lis[i],1+lis[j])
    print(max(lis))

def longestrepchar(st):
    count={}
    l=0
    res=0
    maxf=0
    for r in range(len(st)):
        count[str[r]]=1+count.get(str[r],0)
        maxf=max(count[str[r]],maxf)
        while(r-l+1)-maxf>k:
            count[str[r]]-=1
            l+=1
        res=max(res,r-l+1)

def suduko(grid):
    row =collections.OrderedDict(set)
    cols = collections.OrderedDict(set)
    squares = collections.OrderedDict(set)
    for r in range(9):
        for c in range(9):
            if grid[r][c] in row[r] or grid[r][c] in cols[c] or grid[r][c] in squares[(r//3,c//3)]:
                print("fail")
            row[r].add(grid[r][c])
            cols[c].add(grid[r][c])
            squares[(r//3,c//3)].add(grid[r][c])
        
#median of two array
#no of islands
#minimum window substr



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
    arr = [-2, -1, 5, 10, -5]
    output=asteriodcollision(arr)
    print(output)
