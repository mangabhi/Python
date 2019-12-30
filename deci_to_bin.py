# Python3 program to convert a 
# decimal number to binary number 

def decToBinary(n): 
	
	binaryNum = [0] * n; 
	i = 0; 
	while (n > 0): 

		binaryNum[i] = n % 2; 
		n = int(n / 2); 
		i += 1; 
	for j in range(i - 1, -1, -1): 
		print(binaryNum[j], end = ""); 

n = 17; 
decToBinary(n)
