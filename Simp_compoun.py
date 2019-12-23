#Write a program to enter P, T, R and calculate Simple Interest and compound interest
import math
P=float(input("Enter Principal"))
R=float(input("Enter Rate"))
T=float(input("Enter Year"))

Simp=(P*R*T)/100
print(Simp)

Comp=P*math.pow((1+R/100),T)
print(Comp)
