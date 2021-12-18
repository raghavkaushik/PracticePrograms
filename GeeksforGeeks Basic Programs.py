#1 Python program to add two numbers
import math

a,b=10,45
print("The sum of a+b",a+b)

#2Maximum of two numbers in Python
print("The max in a,b:",max(a,b))

#3Python Program for factorial of a number
def fact(n):
    return 1 if (n==1 or n==0) else n*fact(n-1)

out=fact(5)
print("factorial of a number 5:",out)
print("Factorial using math lib:",math.factorial(4))

#4Python Program for simple interest
#Simple Interest = (P x T x R)/100
p,r,t=10000,5,5
temp=p*r*t
print("Simple Interest:",temp/100)


#5Python Program for compound interest
#A = P(1 + R/100)^ t
#result=A-P
p,r,t=1200,5.4,2
a=p*(pow((1+r/100),t))
print("Compound Interest:",a-p)

#6Python Program to check Armstrong Number
num=153
temp=num
s,r=0,0
while(temp>0):
    r=temp%10
    s=s+(pow(r,3))
    temp=temp//10
if s==num:
    print("Armstrong")

#7 Python Program for Program to find area of a circle
rad=5
print("area of a circle:",3.14*rad*rad)

#8Python program to print all Prime numbers in an Interval
for i in range(2,100):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)

#9 check whether a number is prime or not
num=47
for i in range(2,int(math.sqrt(num))+1):
    if num%i==0:
        break
else:
    print("Prime")

#10Python Program for n-th Fibonacci number
def fib(n):
    if n<=0:
        print("Incorrect")
    if n==1:
        return 0
    if n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

out=fib(10)
print("Fibonacci number:",out)

#11 ASCII Value
c = 'g'
print("The ASCII value of '" + c + "' is", ord(c))


#12 Sum of sqaures
n=5
sm = 0
for i in range(1, n+1) :
    sm = sm + (i * i)
print(sm)

#13 cubes of sqaures
n=5
sm = 0
for i in range(1, n+1) :
    sm = sm + (i * i * i)
print(sm)
