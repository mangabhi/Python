#Description : Write a program to get nth bit of a input number.

def printNthBit(k,n): 
  
    print(k & (1 << (n-1))) 
  
n = 2
k = 13
printNthBit(k,n) 
