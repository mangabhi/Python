#Write a program to swap two numbers using bitwise operator.

a=int(input("Enter a number"))
b=int(input("Enter a number"))
a=a^b
b=a^b
a=a^b
print(a,b)
