# Define a function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".
def eve(n):
    if(n%2==0):
        print("It is even")
    else: 
        print("It is Odd")
    
    return  " " 

n=int(input("Enter a number: "))
print(eve(n))
