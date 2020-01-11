#Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
#Then the function needs to print the last 5 elements in the list.
l=[]
for i in range(1,21):
    d={i:i*i}
    l.append(d)
print(l[15:21])
