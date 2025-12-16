"""li=[1,"shweta",5.4]
print(li)

li=[4,5,2,3,6]
li.sort()
print(li)

li=[4,5,2,3,6]
sorted(li)
print(li)

li=[4,5,2,3,6]
li.append([7,8,9])
print(li)

li=[4,5,2,3,6]
li.extend([8,9,7])
li.sort()
li.append([11,10,12])
li.insert(2,"shweta")
print(li)"""

"""li=[4,5,2,3,6]
print(li[1:4])"""

"""li=[4,5,2,3,6]
sum=0
for num in li:
    sum=sum+num
    print(sum)"""
#find the largest num
"""li=[4,5,2,3,6]
for num in li:
 max(li)
print(max(li))"""

"""li=[4,5,2,3,6]
max_num=li[0]
for current_num in li:
    if max_num<current_num:
        max_num=current_num
print("the lagest value is: ",max_num)"""

"""li=[4,5,2,3,6]
li.sort()
print("the second largest value is: ",li[-2])"""

#["grapes","apple", "banana"] 
"""li_fruits=["grapes","apple", "banana"] 
li_fruits.sort(reverse=False)
print(li_fruits)"""

"""li_fruits=["grapes","apple", "banana","pineaaple"] 
li_fruits.sort(key=len)
print(li_fruits)"""

'''li_fruits=["grapes","apple", "banana","pineaaple"] 
li_fruits.sort(key=len,reverse=True)
print(li_fruits)'''

'''#4->8 or 8->4 swap
li=[4,5,6,7,8]
li[0],li[-1]=li[-1],li[0]
print(li)'''

'''#find the number of odd and even numbers into list
#li=[1,2,3,4]
#number of odd and number of even
li=[1,2,3,4]
even_count=0
odd_count=0

for num in li:
    if num%2==0:
        even_count+=1
    else:
        odd_count+=1
print(f"odd:{odd_count},even:{even_count}")   '''   

# the target is given : 7 you have to find the indices of the elements which sum is 
#equal to
#target
'''li=[8,5,6,7,4]
sum=12
for i in range(len(li)):
    for j in range(i,len(li)):
        if li[i]+li[j]==sum:
         print(i,j)
         break'''

'''li=[8,5,6,7,4]
sum=12
for i in range(len(li)):
    for j in range(i,len(li)):
        if li[i]+li[j]==sum:
         print(i,j)
    break
'''

'''li=[6,5,6,7,4,6]
sum=12
for i in range(len(li)):
    for j in range(i+1,len(li)):
        if li[i]+li[j]==sum:
         print(i,j)
         break
    break'''

#print the duplicate num in list

'''li=[6,5,6,7,4,6]
for i in range(len(li)):
    for j in range(i+1,len(li)):
     if li[i]==li[j]:
      print(li[i])
      continue
    break '''

'''li=[6,5,6,7,4,6]
for i in range(len(li)):
    for j in range(i-1,len(li)):
     if li[i]==li[j]:
      print(set(li))'''

"""li=[1,2,4,5,8,9]
sum=14
for i in range(len(li)):
    for j in range(i,len(li)):
        for k in range(i,len(li)):
         if li[i]+li[j]+li[k]==sum:
          print(i,j,k)
    break"""

'''li=[1,2,4,5,8,9]
li.reverse()
print(li)'''

'''li=[1,2,4,5,8,9]
reverse_li=li[::-1]
print(reverse_li)

li=[1,2,4,5,8,9]
reverse_li=[]
for i in li:
 reverse_li.insert(0,i)
 print(reverse_li)'''

 ##set
'''set={1,2,3}
print(set)

set={1,2,3}
set.add(4)
print(set)'''

'''li=[1,2,3,4,2]
s=set(li)
print(s)'''

'''li=[1,2,3,4,2]
s=set()
for num in li:
    s.add(num)
print(s)'''

'''li=[1,2,3,4,2]
s=set()
for num in li:
    s.add(num)
print(s)
s.remove(3)
print(s)'''

'''li=[1,2,3,4,2]
s=set()
for num in li:
    s.add(num)
print(s)
s.update([5,6,7,8])
print(s)
s.discard(10)
print(s)'''

'''s1={1,2,3,4}
s2={5,6,7,8,9}
s3=s1.union(s2)
print(s3)
s4=s1.intersection(s3)
print(s4)
s5=s4.difference(s2)
print(s5)
s6=s4.symmetric_difference(s3)
s3.clear()
print(s6,s3)'''

'''li=[1,2,2,3,4]
seen=set()
dupicates=set()
for num in li:
    if num in seen:
     dupicates.add(num)
    seen.add(num) 
print(dupicates) ''' 

'''li=[2,3,4,2,5]
for i in range(len(li)):
    for j in range(i+1,len(li)):
        if li[i]==li[j]:
            print(li[i])
            break
    break'''    

'''li=[1,2,4,5,8,9]
sum=14
for i in range(len(li)):
    for j in range(i+1,len(li)):
        for k in range(j+1,len(li)):
         if li[i]+li[j]+li[k]==sum:
          print(li[i],li[j],li[k])'''
    
'''li=[1,2,4,5,8,9]
sum=14
result=[]
for i in range(len(li)):
    for j in range(i+1,len(li)):
        for k in range(j+1,len(li)):
         if li[i]+li[j]+li[k]==sum:
            result.append(li[i])
            result.append(li[j])
            result.append(li[k])
            break
print(result)'''  

"""li=[1,2,4,5,8,9]
sum=14
result=[]
for i in range(len(li)):
    for j in range(i+1,len(li)):
        for k in range(j+1,len(li)):
         if li[i]+li[j]+li[k]==sum:
            result.extend(li[])
            result.extend(li[])
            result.extend(li[])
            break
print(result)"""

'''li=[1,2,3,4,5]
left=0
right=len(li)-1
while left <right:
    li[left],li[right]=li[right],li[left]
    left+=1
    right-=1
print(li)  '''  

'''li=[1,2,3,4,5]
key=5
left=0
right=len(li)-1
key=key%len(li)
while left <right:
    li[left],li[right]=li[right],li[left]
    left+=1
    right-=1
print(li)  
#reverse the list to key-1
left =0
right=key-1
left=0
right=len(li)-1
while left <right:
    li[left],li[right]=li[right],li[left]
    left+=1
    right-=1
print(li)  

left=key
right=len(li)-1
left=0
right=len(li)-1
while left <right:
    li[left],li[right]=li[right],li[left]
    left+=1
    right-=1
print(li)  
'''
'''li=[123,345,789,1001]
sum=0
for num in li:
    while num>0:
     digit=num%10
     sum=sum+digit
     num//=10
    print(sum)'''

'''li=[123,345,789,1001]
product=1
for num in li:
    while num>0:
     digit=num%10
     product=product*num
     num//=10
    print(product)'''

"""li=[1,2,3,4,5]
max_num=0
for num in li:
    if num>max_num:
        max_num=num
print(max_num)"""        

'''li=[1,2,3,4,5]
first_max=0
second_max=0
for num in li:
    if num>first_max:
       second_max=first_max
       first_max=num
    elif num>second_max and num<first_max:
        second_max=num
print(second_max) '''      

'''li=[1,2,3,4,5]
first_max=0
second_max=0
third_max=0
for num in li:
    if num>first_max:
       third_max= second_max
       second_max=first_max
       first_max=num
    elif num>second_max and num!=first_max:
        second_max=num
    elif num>third_max and num!=first_max:
        third_max=num    
print(first_max) 
print(second_max)
print(third_max)'''

'''li=[1,2,3,0,4]
index=0
for i in range(len(li)):
    if li[i]!=0:
        li[index]=li[i]
        index+=1
    while index<len(li):
        li[index]=0
        index+=1
print(li)  '''          

'''sentence="python is a good"
reversed_sentence=''.join(sentence.split()[::-1])
print(reversed_sentence)'''

'''sentence="python is good".split()
print(sentence)
sentence.reverse()
reversed_sent=' '.join(sentence)
print(sentence)'''

"""li=list(map(int,input("enter the list of numbers").split()))
print(li)"""
"""
li=list(map(int,input("enter the list of numbers").split()))
total=sum[li]
print(total)"""

'''li = list(map(int, input("Enter the list of numbers: ").split()))
total = sum(li)
print("Sum:", total)'''