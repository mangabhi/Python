#Description : Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included).

def printTuple():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print (tuple(li))
		
X=printTuple()
print(X)
