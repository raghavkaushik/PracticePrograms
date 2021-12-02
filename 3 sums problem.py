
#The sum of 3 value must be equal to zero

arr=[-1,0,1,2,-1,-4]
arr.sort()
result=[]
for i,a in enumerate(arr):
    if i>0 and arr[i-1]==arr[i]:
        continue
    low=i
    high=len(arr)-1
    while(low<high):
        total=arr[low]+arr[high]+a
        if total<0:
            low+=1
        elif total>0:
            high-=1
        else:
            result.append([arr[low],arr[high],a])
            low+=1
            while(arr[low]==arr[low-1] and low<high):
                low+=1


print(result)
