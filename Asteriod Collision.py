#Asteriod Collision problem
#As per common leetcode problems

arr=[-2,-1,5,10,-5]
result=[]
for i in range(len(arr)):
    if arr[i]<0 and len(result)>0 and result[-1]>0:
        if abs(arr[i])<result[-1]:
            break
        if abs(arr[-1])==result[-1]:
            result.pop(-1)
            break
        else:
            result.pop(-1)
            continue
    else:
        result.append((arr[i]))

print("Asteriod Collision Problem:",result)