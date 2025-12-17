'''class housebuilding:
  color='white'
  price=500000
tushar_house=housebuilding()
print(tushar_house.color)
h2=housebuilding()
print(h2.color,h2.price)
print(housebuilding.price)
h2.price=600000
print(h2.price)
housebuilding.price=700000
h3=housebuilding()
print(h3.price)
print(h2.price)'''


'''class house:
 
    color='white'
    price=500000
    
    def info(self):
      print("house has price",self.price,house.price)
tushar_house=house()
tushar_house.info()
h2=house()
h2.info()
house.price=600000
h2.info()'''

'''class studentdetail:
    student_name="shweta"
    student_id=223445
    student_fees=50000
    student_email="shweta@gmail.com"
    def info(self):
     print("student name",self.student_name)
     print("student id",self.student_id)
     print("student fee",self.student_fees)
     print("student email",self.student_email)
shweta=studentdetail()
shweta.info()'''

'''class housebuilding:
  def __init__(self):
    print("constructor calling",self)
h1=housebuilding()
print(h1)
h2=housebuilding()
print(h2)'''

'''class housebuilding:
  def __init__(self,a):
    self.a=a           # self.color is instance variable.
h1=housebuilding("black")
print(h1.a)
h2=housebuilding("green")
print(h2.a)'''

'''class housebuilding:
  def __init__(self,color,price):
    self.color=color
    self.price=price
h3=housebuilding("white", 60000)
print(h3.color,h3.price)'''

'''class A:
  count=0
  def __init__(self):
    A.count+=1
a1=A()
print("value =",a1.count)
a2=A()
print("value =",a2.count)
a3=A()
print("value =",a3.count)'''


'''class A:
  num=300
  def infoa(self):
    print("A class has data",self.num)
class B(A):
  amount=500
  def infob(self):
    print("B class has data",self.amount,self.num)
    self.infoa()
b1=B()
b1.infob() #object.info()'''

'''class UberCustomer:
  Company="UBER PRIVATE LIMITED"
  def __init__(self,name,wallet):
    self.name=name
    self.wallet=wallet
  def info(self):
    print("information of uber is = '",self.name,"' '",self.wallet,"'")
Uc1=UberCustomer('naina',766)
Uc1.info()

class UberDriver(UberCustomer):
  def __init__(self,name,wallet):
    super().__init__(name,wallet)
  def info2(self):
    super().info()
Ud1=UberDriver('driver shyam',776)
print(Ud1.Company)
Ud1.info2()'''

'''class A:
  x='name1'
class B(A):
  y='name2'
class C(B):
  z='name3'
a=A()
print(a.x)
b=B()
print(b.x)
c=C()
print(c.z)'''


'''class A:

  def __init__(self):
    print("hello")
class B(A):
  def __init__(self):
    super().__init__()
class C(A):
  def __init__(self):
    super().__init__()

obj1=A()
obj2=B()
obj3=C()'''

'''class UncleA:
  x='shyam'

class UncleB:
  y='shivam'

class ChildC(UncleA,UncleB):
  z=500
  p=1000

a=UncleA()
print(a.x)
b=UncleB()
print(b.y)
c=ChildC()
print("give a money ::\n","UncleA =",a.x,c.z,"\n","UncleB =",b.y,c.p)'''


'''class UncleA:
  x='shyam'
  def infoa(self):
    print("A class has data",self.x)

class UncleB:
  y='shivam'
  def infob(self):
    print("A class has data",self.y)

class ChildC(UncleA,UncleB):
  z=500
  p=1000
c=ChildC()
a=UncleA()
print(c.x)
b=UncleB()
print(c.y)
c.infoa()
c.infob()
print("give a money ::\n","UncleA =",a.x,c.z,"\n","UncleB =",b.y,c.p)'''

'''class Home:
    def info(self):
        print("hey home class has white color")
class userHome:
    pin=1024
    def info(self):
        print("hey user home class has yellow color")
UH1=userHome()
UH1.info()'''

'''class RBI:
    def info(self):
        print("the interest is 5%")
class HDFC():
    def info(self):
        print("the interest is 10%")
obj=HDFC()
obj.info() '''              

from abc import ABC,abstractmethod
#abc=> package,ABC=abstract base class
class RBIBANK(ABC):                #here rbi is abstract class which inherit the abstract base class
  def __init__(self,loanamount):
    self.loanamount=loanamount
  @abstractmethod
  def interestrate(self):
    pass
class SBIBANK(RBIBANK):
  def __init__(self,loanamount):
    super().__init__(loanamount)
sb1=SBIBANK(5000)
sb1.interestRate()
