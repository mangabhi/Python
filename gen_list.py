# Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).
def printValues():
	l = []
	for i in range(1,21):
		l.append(i**2)
	print(l[:5])
	print(l[-5:])

printValues()
