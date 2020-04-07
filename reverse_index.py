#reversing string and get the postion elemnt index
l=[int(x) for x in input("Enter multiple varaible: ").split(',')]
res=[0]*len(l)
k=2

for i in range(len(l)):
    if(i+k)<len(l):
        res[i+k]=l[i]
    else:
        pol=(i+k)%len(l)
        res[pol]=l[i]
print(res)
x=5
for p in range(len(res)):
    if res[p]==x:
        print(res.index(x))        
