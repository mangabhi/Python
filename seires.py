#0,0,7,6,14,12,21,18, 28
a=6
b=7
c=1
val=1
val2=1
mylist=[0,0]
k=int(input())
while c<k:
    if c%2==0:
        mylist.append(a*val)
        val+=1
        c+=1
        
    else:
        mylist.append(b*val2)
        val2+=1
        c+=1
        
print(mylist)


#1,1,2,3,4,9,8,27,16,81,32,243,….
a=3
b=2
c=1
val=1
val2=1
mylist=[1,1]
k=int(input())
while c<k:
    if(c%2==0):
     mylist.append(a*val)
     val*=a
     c+=1
    
    else:
     mylist.append(b*val2)
     val2*=b
     c+=1
print(mylist)    

#1,1,2,2,4,4,8,8,16,16
a=2
b=2
c=1
val=1
val2=1
mylist=[1,1]
k=int(input())
while k>c:
    if(c%2==0):
     mylist.append(a*val)
     val*=a
     c+=1
    
    else:
     mylist.append(b*val2)
     val2*=b
     c+=1
print(mylist)    







A=int(input("Enter a number: "))
lis=[int(input("Enter %d number")) for x in range(A)]
print("unsorted array : ",A)

for i in range(len(A)-1):
    temp=i
    for j in range(i+1,len(A)):
        if A[temp]>A[j]:
            temp=j
    #min_ind=A.index(temp,i)
    if A[i]!=A[temp]:
        
        A[i],A[temp]=A[temp],A[i]
print(A)


'''

A=[34,21,45,78,2,42,21]
print("unsorted list",A)

for j in range(len(A)-1):
    for i in range(len(A)-1-j):
        if A[i]>A[i+1]:
            A[i],A[i+1]=A[i+1],A[i]
        
        else:
            print(A)
        print()    
print(A)    '''
