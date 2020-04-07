arr=[int(x) for x in input("Enter multiple input").split(',')]
rotat=[0]*len(arr)
k=2   #depends upon the number of rotation you want
for i in range(len(arr)):
    if i+k<len(arr):
        rotat[i+k]=arr[i]
    else:
        back_ele=(i+k)%len(arr)
        rotat[i+k]=arr[i]
print(rotat)        
