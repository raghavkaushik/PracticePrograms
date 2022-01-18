#Sorting and Searching

def mergesort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]
        mergesort(left)
        mergesort(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]>right[j]:
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=arr[j]
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

    return arr

def quicksort(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot=arr.pop()
    items_greater=[]
    items_smaller=[]
    for item in arr:
        if item > pivot:
            items_greater.append(item)
        else:
            items_smaller.append(item)
    return quicksort(items_smaller)+[pivot]+items_greater

def bubblesort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

def binarysearch(arr,l,h,val):
    if h>=l:
        mid=l+(h-l)//2
        if arr[mid]==val:
            return val
        elif arr[mid]>val:
            return binarysearch(arr,l,mid-1,val)
        elif arr[mid]<val:
            return binarysearch(arr,mid+1,h,val)
        else:
            return -1

#linked list: insert, delete, lookup, print, delete alterante, reverse, sum of 2, merge 2, remove duplicate,
class node:
    def __init__(self, data):
        self.next=None
        self.data=data

class linkedlist:
    def __init__(self):
        self.root=None

    def insertll(self,data,pos):
        if self.root is None:
            self.root=node(data)
        if self.root is not None and pos==1:
            temp=self.root
            self.root=node(data)
            self.root.next=temp
        if self.root is not None and pos>1:
            current=self.root
            count=1
            while current:
                if count==pos:
                    temp=node(data)
                    prev.next=temp
                    next.next=current
                prev=current
                current=current.next

    def deletell(self,data):
        if self.root is None:
            return False
        current=self.root
        while current:
            if current.data==data:
                prev.next=current.next
            prev=current
            current=current.next

    def lookupll(self,data):
        if self.root is None:
            print("Empty Linked list")
            return False
        else:
            current=self.root
            while current:
                if current.data==data:
                    return current
                current=current.next

    def removealternate(self):
        if self.root is None:
            return False
        else:
            current=self.root
            count=1
            while current.next:
                if count%2==0:
                    prev.next=current.next
                prev=current
                current=current.next
                count+=1
        return True

    def reversell(self):
        if self.root is None:
            return False
        else:
            prev=None
            temp=None
            current=self.root
            while current:
                next=current.next
                current.next=prev
                prev=current
                current=next
            self.root=prev

    def mergetwo(self,head1,head2):
        if head1 == None and head2 != None:
            return head2
        if head1 != None and head2 == None:
            return head1
        prev = None
        while head1 is not None and head2 is not None:
            if head1.data==head2.data:
                prev=head1
                head1=head1.next
            if head1.data>head2.data:
                prev=head2.data
                head2=head2.data
            if head1.data<head2.data:
                prev=head1.data
                head1=head1.next
            if head1 == None:
                prev = head2
            if head2 == None:
                prev = head1
            prev=prev.next