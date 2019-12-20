# Write a program to check whether a number is even or odd using bitwise operator.


n=int(input("Enter a number"))
if(n&1==0):
    print("Even")
else:
    print("Odd")
