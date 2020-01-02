#Description : Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).
		
li = [1,2,3,4,5,6,7,8,9,10]
squaredNumbers = map(lambda x: x**2, li)
print squaredNumbers
