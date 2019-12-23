'''"Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9"
'''

n=str(input("Ebter a string"))
u=l=0
for i in n:
    if i.isupper():
        u+=1
    elif i.islower():
        l+=1
    else:
        pass
print(u)
print(l)
