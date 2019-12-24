m=int(input("Enter a number"))
p=int(input("Enter a number"))

for n in range(m,p):
    if n>1:
        for i in range(2,n):
            if(n%i==0):
                #print(n,"is not prime number")
                break;
        else:
            print(n)
    
    
    
