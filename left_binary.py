
# Simple Python3 program  
# to find MSB number 
# for given n. 
def setBitNumber(n): 
    if (n == 0): 
        return 0; 
  
    msb = 0; 
    while (n > 0): 
        n = int(n / 2); 
        msb += 1; 
  
    return (1 << msb); 
  
# Driver code 
n = 0; 
print(setBitNumber(n));
