#Write a program to create gcd and lcm 
def gcd(a,b):
    if a==0:
        return b;
    return gcd(b%a,a);



def lcm(a,b):
    return (a*b)/gcd(a,b);

a=int(input("Enter a number"))
b=int(input("Enter a number"))
print(gcd(a,b))    
print(lcm(a,b))
