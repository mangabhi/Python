#Remove Even Integers from List
#Here is used two method for solving this code
#Using remove and append

a=[2,5,7,9,3,1,6,73,12]
for i in a:
    if i%2==0:
        a.remove(i)
print(a)        

a=[2,5,7,9,3,1,6,73,12]
l=[]
for i in a:
    if i%2==1:
        l.append(i)
print(l)        
