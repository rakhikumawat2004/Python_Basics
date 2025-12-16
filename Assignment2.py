#question 1
n=int(input("enter n: "))
for i in range(1,n+1):
    print(i)

#question 2
n=int(input("enter n: "))
for i in range(n,0,-1):
    print(i) 

#question 3
for i in range(97,123):
    print(chr(i)) 

#question 4
a=100
for i in range(2,a+1,2):
    if(i%2==0):
     print(i) 

#question 5
n=int(input("enter n: "))
sumodd=0
for i in range(1,n+1):
    if(i%2!=0):
     sumodd+=i
     print("sumodd",sumodd) 
     
     #question 6
num=int(input("enter n: "))
count=0
for digit in str(num):
     count+=1
     print("numberof digits",count)

#question 7
num=int(input("enter n: "))
sumdigits=0
for digits in str(num):
     sumdigits+=int(digits)
     print("sum of digits :",sumdigits)                         