#Leap year
#1ST method
n=int(input("Enter a number: "))
if(n%4==0):
    if(n%100==0):
        if(n%400==0):
            print("Leap year")
        else:
            print("Non Leap year")
    else:
        print(" Leap year")
else:
    print("Non Leap year")    
    
    
2ND MEthod

n=int(input("Enter a number: "))
if(n%4==0)and(n % 100 != 0 or n % 400 == 0):
    print("Leap year")
else:
    print("Non Leap")
