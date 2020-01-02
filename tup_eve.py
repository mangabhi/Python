#Description : Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10)

a=(1,2,3,4,5,6,7,8,9,10)
for i in range(len(a)):
    if a[i]%2==0:
        print(a[i],sep=" ",end=",")
