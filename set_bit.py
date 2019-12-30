#Description : Write a program to set nth bit of a number.

num=int(input("Enter any number: "))
n=int(input("Enter any number(0-31): "))
newNum=(1<<n)|num
print("Number before seting bit: ",n,num)
print("Number after setting bit: ",n,newNum)
