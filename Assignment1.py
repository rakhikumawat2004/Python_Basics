#question 1

n=int(input("enter n :"))
if(n%2==0):
 print("even")
else:
  print("odd")


#question 2
a=10
b=20
c=30
if(a>b and a>c):
  greatest = a
elif(b>a and b>c):
  greatest=b
else:
  greatest =c
  print("greatest number",greatest)


#question 3
x=int(input("enter x "))
if(x%4==0 and x%100!=0 or x%400==0):
 print("leap year")
else:
  print("not leap year")


#question 4
x=int(input("enter x "))
if(x>=90):
  print("grade A")
elif(x>=80):
  print("grade B")
elif(x>=70):
  print("grade C")
elif(x>=60):
  print("grade D")
else:
  print("grade F")


#question 5
  n=input("enter n :")
if(n in "aeiou"):
  print("vowel")
else:
  print("consonant")


#question 14
x=int(input("enter x "))
if(x<=1):
  print("Infant")
elif(x<=4):
  print("Todler")
elif(x<=12):
  print("Child")
elif(x<=19):
  print("Teenager")
elif(x<=59):
  print("Adult")
else:
  print("senior")


#question 8
  username=input("enter username ")
password=input("enter password ")
if(username=="admin" and password=="1234"):
    print("login successfull")
else:
  print("login failed")


#question 6
  num1=float(input("enter num1: "))
operator=input("enter operator(+,-,*,/): ")
num2=float(input("enter num2: "))
if(operator=="+"):
  result=num1+num2
  print("result",result)

elif(operator=="-"):
  result=num1-num2
  print("result",result)

elif(operator=="*"):
  result=num1*num2
  print("result",result)

elif(operator=="/"):
  result=num1/num2
  print("result",result)

else:
  print("invalid operator")


#question 9
a=int(input("enter a: "))
b=int(input("enter b: "))
c=int(input("enter c: "))
if(a+b>c and b+c>a and a+c>b):
  print("tringle is valid")
else:
  print("tringle is not valid")     


  x=int(input("enter x: "))
if(x>=1000):
  print("discount is 10%")
elif(1000>=x>=500):
  print("discount is 5%")  
else:
  print("no discount")  


#question 10
  weight=float(input("enter wieght(in kilogram): ")) #kilogram
height=float(input("enter height(meter): ")) #meter
BMI = weight / (height ** 2)
if(BMI < 18.5):
  print("Underweight")
elif(18.5 <= BMI < 24.9):
  print("Normal weight")
elif(25 <= BMI < 29.9):
  print("over weight")
elif(BMI >= 30):
  print("Obesity")


#question 15
  x=int(input("enter x: "))
days=["monday","tuesday","wednesday","thrusday","friday","saturday","sunday"]
if(1<=x<=7):
 print("day of the weak: ",days[x-1])
else:
  print("input invalid")


#question 7
  x=int(input("enter x: "))
if(x>0):
  print("positive")
elif(x==0):
  print("zero")
else:
  print("negative")    


#question 12
  x=int(input("enter x: "))
year=["january","february","march","april","may","june","july","august","september","october","november","december"]
if(1<=x<=13):
 print("month of the year: ",year[x-1])
else:
  print("input invalid")


  #question 13
  balance=1000
x=input("enter your choice: ")
if(x=="1"):
  print("your current balance is:",balance)
else:
  if(x=="2"):
   amount=int(input("enter your deposite amount:"))
   if(amount>0):
    balance+=amount
    print("new balance is",balance)
   else:
    print("enter your valid amount")  
  else:
    if(x=="3"):
     amount=int(input("enter your withdraw money:"))
     if(amount>0):
      if(balance>=amount):
       balance-=amount
       print("new balance is",balance)
      else:
        print("not enough balance")
     else:
      print("enter your valid amount") 
    else:
     print("invalid choice")

   