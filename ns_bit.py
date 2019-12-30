#Description : Write a program to clear nth bit of a number.

num=int(input("Enter a number: "))
n=int(input("Enter a number: "))
bitStatus = (num >> n) & 1;
print("The bit is set to", n, bitStatus);
