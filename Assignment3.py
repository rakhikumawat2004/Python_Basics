"""#question 1
n=int(input("enter n: "))
i=0
while(i<n):
    i+=1
    print(i)

#question 2
n=int(input("enter n: "))
i=n
while(i>0):
    i-=1
    print(i)"""

"""#question 3
i=96
while(i<122):
    i+=1
    print(chr(i)) 

#question 4
i=0
while(i<100):
    if(i%2==0):
     i+=2
     print(i)

#question 5
n=int(input("enter n: "))
i=0
odd=0
while(i<=n):
 if(i%2!=0):
   odd+=i
 i+=1
print("sum of odd numbers", odd)
     
#question 6
n=int(input("enter n: "))
i=0
count=0
while(i<n):
  n=n//10
  count+=1
print("number of digits",count)

#question 7
c"""

"""#question 8
num=int(input("enter num: "))
orignal_num=num
last_digit=num%10
while(num>=10):
    num=num//10
first_digit=num
print("first digit",first_digit)
print("last digit",last_digit)"""

"""#question 9
num=int(input("enter num: "))
orignal_num=num
sum_digit=0
last_digit=num%10
while(num>=10):
    num=num//10
first_digit=num
sum_digit=first_digit+last_digit
print("first digit",first_digit)
print("last digit",last_digit)
print("sum of digits",sum_digit)"""

"""#question 10
num=int(input("enter num: "))
orignal_num=num
reversed_num=0
while(0<num):
    digit=num%10
    reversed_num=reversed_num*10+digit
    num=num//10
print("reversed_num",reversed_num)"""

"""#question 11
num=int(input("enter num: "))
exponent=int(input("enter exponent: "))
orignal_exponent=exponent
power=1
while(exponent!=0):
    power=power*num
    exponent-=1
print(f"result: {num}^{orignal_exponent}={power}") """   

"""#question 12
num=int(input("enter num: "))
print("factors of num: ")
i=1
while(i<=num):
    if(num%i==0):
        print(i)
    i+=1"""

"""#question 13
num=int(input("enter num: "))
print("factorial of num is : ")
factorial=1
while(num!=0):
    factorial*=num
    print(num)
    num-=1
print(factorial)"""

 #question 14
num1=int(input("enter num1: "))
num2=int(input("enter num2: "))
a=num1
b=num2
while(b!=0):
    a,b=b,a%b
    gcd=a
    lcm=num1*num2//gcd
print(f"lcm {num1} and {num2} is:{lcm}")

    
