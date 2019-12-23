'''"Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3"'''

p=input("Enter a value")
d=l=0
for i in p:
    if i.isdigit():
        d+=1
    elif i.isalpha():
        l=l+1
    else:
        pass
print(d)
print(l)
