#Description : Write a program to get lowest set bit of a number.

INT_SIZE=32
num=int(input("enter a number"))
order=INT_SIZE-1
for i in range(0,INT_SIZE):
    if((num>>1)&1):
        order=i
        break;

print("lowest set bit "num,order)        
    
        
