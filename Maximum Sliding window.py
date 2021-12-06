#To find the maximum in a sliding window of 3, consider the max in the size of 3 until the index moves out.
#Queue stores the indexes of the array.

from collections import deque
arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
result=[]
left=right=0
k=3
queue=deque()
while(right<len(arr)):
    while(queue and arr[queue[-1]]<arr[right]):
        queue.pop()
    queue.append(right)
    if left>queue[0]:
        queue.popleft()
    if right+left>=k:
        result.append(arr[queue[0]])
        left+=1
    right+=1

print("The maximum in a sliding window of 3:",result)