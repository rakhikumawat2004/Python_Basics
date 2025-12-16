"""a=79
count=0
while(a>63):
  if(a%2==0):
    count+=1
  a-=1

print("count",count)  

count=0
i=1
while(count<5):
  if(i%2==0 and i%3==0):
    count+=1
    print(i)
  i+=1    """


"""for i in range(1,6):
    if(i==4):
        break
    print(i)
print("hello")  

for i in range(1,6):
    if(i==4):
     continue
    print(i)
print("hello")  """

"""for i in range(1,8):
    if(i%2==0):
     continue
    print(i)
print("hello")"""

"""num=11
i=2
detective=0
while(i<num):
 if(num%i==0):
  detective=1
  break
 i+=1
 if(detective==1):
  print("loop break hence not prime")
 else:
  print("prime") """

"""n=153
total=0
temp=n
while(n>0):
    rem=n%10
    n=n//10
    total+=rem**3
    print(n,total) 
if(temp==total):
    print("amstrong")
else:
    print("not") """  

"""s="abcd"
i=0
while(i<4):
    print(i,s[i])  
    i+=1       

s="abcdefghi"
i=0
while(i<len(s)):
    print(i,s[i])  
    i+=1 """ 

"""s="abcdefghijklm"
j=len(s)-1
while(j>=0):
    print(j,s[j])  
    j-=1 """     

"""s="abcdefghijklmnopqrstuvwxyz"
i=0
j=len(s)-1
while(i<len(s)):
    print(i ,s[i] ,s[j])  
    i+=1
    j-=1"""

"""s="abcbd"
i=0
j=len(s)-1
while(i<len(s)): 
    if(s[i] == s[j]):
        print("true" ,s[i] , s[j])
    else:
        print("false" ,s[i] , s[j])    
    i+=1
    j-=1"""

"""s="abcbd"
i=0
j=len(s)-1
while(i<=len(s)//2): 
    if(s[i] == s[j]):
        print("true" ,s[i] , s[j])
    else:
        print("false" ,s[i] , s[j])    
    i+=1
    j-=1"""

"""s="abcbd"
i=0
j=len(s)-1
while(i<=j): 
    if(s[i] == s[j]):
        print("true" ,s[i] , s[j])
    else:
        print("false" ,s[i] , s[j])    
    i+=1
    j-=1 

s="saras"
i=0
j=len(s)-1
a=0
while(i<=j): 
    if(s[i] != s[j]):
        a=1
        break
    i+=1
    j-=1
if(a==1):  
        print("not a palidrom")
else:
        print("palidrom")    

    
a=2
b=15
if(a>b):
  c=a
else:
   c=b
while(True):  
 if(c%a==0 and c%b==0):
  print("lcm",c)
  break
 else:
  c+=1
print(c)

a=10
b=15
if(a<b):
  c=a
else:
   c=b
while(True):  
 if(c%a==0 and c%b==0):
  print("hcf",c)
  break
 else:
  c-=1
print(c)

for i in range(1,4):
    print("student",i)
    for j in range(1,6):
     print("subject",j)"""

"""name="shweta"
i=0
while i<5:
    i+=1
    if i==3:
     continue
    print(i)"""   

"""for i in range(5):
    for j in range(5):
        print(f"[{i},{j}]", end=" ")
    print()"""

"""for i in range(5):
    for j in range(7):
        print(f"[{i},{j}]", end=" ")
    print()"""

"""for i in range(4): #rows
    for j in range(4): #column
        print(" * ", end=" ")
    print()"""
"""
for i in range(4): #rows
    for j in range(4): #column
        if i>=j:
         print(" * ", end=" ")
    print()"""


"""for i in range(4): #rows
    for j in range(4): #column
        if i<=j:
         print(" * ", end=" ")
    print()  """ 

"""for i in range(5): #rows
    for j in range(i+1): #column
         print(j, end=" ")
    print()"""

"""for i in range(5): #rows
    for j in range(i+1): #column
         print(f"{i}", end=" ")
    print()"""

"""num=1
for i in range(5): #rows
    for j in range(i+1): #column
         print(f"{num}", end=" ")
         num+=1
    print()"""

"""for i in range(5,0,-1): #rows
    for j in range(1,i+1): #column
         print(j, end=" ")
    print()"""

"""num=1
for i in range(5,0,-1): #rows
    for j in range(1,i+1): #column
         print(f" {num} ", end=" ")
         num+=1
    print()"""    

"""for i in range(5): #rows
    for j in range(5-i): #column
         print(" * ", end=" ")
    print()"""

"""for i in range(5): 
    # this loop is for spaces
    for j in range(5-i): 
           print(" ", end=" ")
    # this loop is for star
    for j in range(i*2+1):
           print("*", end=" ")  
    # this loop is for spaces
    for j in range(5-i): 
           print(" ", end=" ")           
    print()"""

'''for i in range(5): 
    # this loop is for spaces
    for j in range(i+1): 
           print(" ", end=" ")
    # this loop is for star
    for j in range(2*5-(2*i+1)):
           print("*", end=" ")  
    # this loop is for spaces
    for j in range(i+1): 
           print(" ", end=" ")           
    print()'''

'''li = [1, 2, 2, 3, 4]
seen = []
duplicates = []

for num in li:
    if num in seen:
        if num not in duplicates:
            duplicates.append(num)
    else:
        seen.append(num)

print(duplicates)'''
'''
li = [1, 2, 1, 3, 4]
seen = []
duplicates = []
for num in li:
    if num in seen:
        if num not in duplicates:
            duplicates.append(num)
    else:
        seen.append(num)
print(duplicates)'''

'''li = [1, 2, 3, 4, 5]
key = 9'''

'''# Step 0: Normalize key
key = key % len(li)  # key = 0

# Step 1: Reverse first 'key' elements
left = 0
right = key - 1
while left < right:
    li[left], li[right] = li[right], li[left]
    left += 1
    right -= 1
print(li)    

# Step 2: Reverse the rest
left = key
right = len(li) - 1
while left < right:
    li[left], li[right] = li[right], li[left]
    left += 1
    right -= 1
print(li)    

# Step 3: Reverse the whole list
left = 0
right = len(li) - 1
while left < right:
    li[left], li[right] = li[right], li[left]
    left += 1
    right -= 1

print(li)'''


li=[1,2,3,4,5]
first_max=0
second_max=0
third_max=0
fourth_max=0
for num in li:
    if num>first_max:
       fourth_max=third_max
       third_max= second_max
       second_max=first_max
       first_max=num
    elif num>second_max and num!=first_max:
        second_max=num
    elif num>third_max and num!=first_max:
        third_max=num  
    elif num>fourth_max and num!=first_max:
        fourth_max=num       
print(first_max) 
print(second_max)
print(third_max)
print(fourth_max)

