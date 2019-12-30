# Python3 code to toggle k-th bit of n 

def toggleKthBit(n, k): 
	return (n ^ (1 << (k-1))) 
	

n = 5
k = 1
print( toggleKthBit(n , k)) 

