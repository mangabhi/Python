#Description : Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line.


def abc(s1,s2):
    a=len(s1)
    b=len(s2)
    if s1>s2:
        print(s1)
    elif s2>s1:
        print(s2)
    elif s1==s2:
        print("Equal string")
    else:
        print("Wrong entry")
    return " "   

s1=input("Enter a string")
s2=input("Enter a string")
print(abc(s1,s2))
