#Description : Write a program to flip bits of a binary number using bitwise operator.

import math 
  
def invertBits(num):    
    x = int(math.log2(num)) + 1
  
    # Inverting the bits one by one  
    for i in range(x):  
        num = (num ^ (1 << i))  
      
    print(num)  
num = int(input("Enter a number"))
invertBits(num)  
