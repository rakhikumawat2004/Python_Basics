'''list1 = [2, -7, 5, -64, -14]

pos = 0
neg = 0

for num in list1:
    if num > 0:
        pos += 1
        print("Positive numbers:", pos)
    elif num<0:
       neg +=1
       print("Negative numbers:", neg)'''

'''
count=0
for x in range(1,60):
  if(x%2==0 and x%3==0):
    count+=1

print("Count", count)'''

'''def func(num):
  for i in range(2, num):
    if(num%i==0):
      return "not prime"

  return "prime"
func(6)
print(func)'''

'''n=5
triangle=[]
for i in range(n):
    row=[1]*(i+1)
    for j in range (1,i):
        row[j]=triangle[i-1][j-1]+triangle[i-1][j]
    triangle.append(row)
for k in range(n):
    print(" "*(n-k-1),end=" ")
    for t in triangle: 
        print(t)'''

'''names={"aman":87458541 ,  "ishan":9745821}
print( names["ishan"] )
names["ishan"]=65739912   #updated number
names["kajal"]=3459102   #insert data
print(names)
print(names)

a=names.pop('aman')   # a have mobile number of aman

print(names)
print("a:",a)'''

'''mydictionary={"b":20000, "a":7000}
mydictionary["a"]=mydictionary["a"]+5000
mydictionary["c"]=90001
print(mydictionary)'''

'''a={}
for i in [10,20,30,10,40,50]:
    detective=0
    for j in a:
        if(i==j):
             detective=1
    if(detective==0):
        a[i]=1
    else:
        a[i]=a[i]+1
print(a) '''  

'''str1="regexian"
str2="tushar"
str3=" "
for i in range(0,len(str1)):
    for j in range(0,len(str2)):
        if(str1[i]==str2[j]):
            str3=str3+str1[i]

print(str3)'''

'''a = {"total": 0}

for i in range(1, 88):  # loop from 1 to 87
    if i % 2 == 0:      # check if number is even
        a["total"] += 1 # increase the total count by 1

print(a)'''

'''student ={
"name" ="Tushar",
"age" =20,
"course" = "Python"
}

print(student.get("course"))'''
'''student = {
    "name": "Tushar",
    "age": 20,
    "course": "java"
}

print(student.get("course"))'''

'''student = {
    "name": "Tushar",
    "age": 20,
    "course": "java"
}
if "name" in student:
    print("Key exists")
#print(student.keys())
#print(student.values())
#print(student.items())'''
'''for key, value in student.items():
    print(key, ":", value)
print(len(student))
student.clear()
print(student)
copy_dict = student.copy()
print(copy_dict)'''
'''students = {
    "stud1": {"name": "Aman", "age": 18},
    "stud2": {"name": "Naina", "age": 19}
}
print(students)
a = {"x": 1, "y": 2}
b = {"z": 3}
a.update(b)
print(a)
'''
'''marks = {"math": [80, 90, 85], "science": [75, 88, 92]}
print(marks)'''
'''word = "banana"
freq = {}
for ch in word:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)

word = "banana"
freq = {}
for ch in word:
    if ch not in freq:
        freq[ch]=1
    else:
        freq[ch]=freq[ch]+1   
print(freq)

word ="banana"
a={}
for ch in word:
    detective=0
    for j in a:
        if(ch==j):
             detective=1
    if(detective==0):
        a[ch]=1
    else:
        a[ch]=a[ch]+1
print(a)'''

'''scores = {"Aman": 78, "Tina": 92, "Ravi": 85}

topper = {}
highest = 0

for name, mark in scores.items():
    if mark > highest:
        highest = mark
        topper = name

print("Topper:", topper)'''

'''t6 = (1, 2, 3)
temp = list(t6)
temp[0] = 100
t6 = tuple(temp)
print(t6)'''

'''t7 = (1, 2) + (3, 4)
print(t7)

t9 = (1, 2, 3, 4, 5)
print(5 in t9)  # True

t10 = (10, 20, 30, 40, 50)
print(len(t10))
'''
'''
t11 = (10, 20, 30)
a, b, c = t11
print(a, b, c)'''

'''t12 = (1, 2, (5, 6, 7, 8), 9)
print(t12[2][1]) ''' 
'''t15 = (1, 2, 3, 4, 5)
print(t15.index(4))'''


'''lst = [1, 2, 3, 4]
t16 = tuple(lst)
print(t16)
t17 = (10, 20, 30)
lst2 = list(t17)
print(lst2)
t18 = (1, 2, 3, 4)
for item in t18:
    print(item)'''
'''t19 = (3, 1, 4, 2)

# Convert tuple to list because tuples are immutable
lst = list(t19)

# Bubble sort
for i in range(len(lst)):
    for j in range(0, len(lst)-i-1):
        if lst[j] > lst[j+1]:
            # Swap elements
            lst[j], lst[j+1] = lst[j+1], lst[j]

# Convert back to tuple
sorted_t19 = tuple(lst)
print(sorted_t19)'''

t20 = (1, "Hello", [2, 3, 4])
print(t20)
