#1 Python Program to find sum of array
arr=[5,6,7,3,2,7,9]
print("Sum of Array 1:", sum(arr))

#2 Python Program to find largest of array
arr=[5,6,7,3,2,7,9]
print("Sum of Array 1:", max(arr))

#3Python Program for array rotation
n=len(arr)
d=2
arr[:]=arr[d:n]+arr[0:d]
print(arr)

#4 Python Program for Reversal algorithm for array rotation
arr=arr[::-1]
print(arr)

#5 array is monotonic
#out=all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or all(A[i] >= A[i + 1] for i in range(len(A) - 1))