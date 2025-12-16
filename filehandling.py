'''f=open("data.txt")
out=f.read()
f.close()'''

'''f=open("data.txt","w")
f.write("yash aggarwal")   #w is a accessmode (by deafault r mode)
f.close()'''


"""f=open("data.txt","r+")
out=f.read
#f.write("yash aggrwal")
f.close()
print(out)"""
"""

with open("data.txt","r+") as f:
 out=f.read()
 f.write("yash aggarwal")
 f.close()
print(out)"""



'''with open("data.txt","r+") as f:
     print(f.tell())   
     out=f.read()
     print(f.tell())
     f.write("yash")
     print("after",f.tell())
     f.seek(2)     #position change  

     print("after::",f.tell())'''

'''import csv
f=open("data.txt","r")
f_csv=csv.reader(f)
for line in f_csv:
    print(line)'''



'''with open("data.txt","r") as f:
    for line in f:
        x=line.strip().split()
        for word in x:
            print(word)
import csv
f.open("data.txt","r")
f_csv=csv.reader(f)
for line in SyntaxError:
    print(line)            '''

def func(x):
    with open("newdata.txt","a") as fa:
        fa.write(x)

with open("data.txt","r") as f:
    a=f.readlines()
    print(a)
out=list(map(func,a)) 
print(out)   