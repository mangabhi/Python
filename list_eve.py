#Description : Please write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24].
a=[5,6,77,45,22,12,24]
for i in range(len(a)):
    if a[i]%2!=0:
        print(a[i],sep=" ",end=",")
