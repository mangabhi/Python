#Bubble sort
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    
arr=[3,2,8,1,9,3,0]
bubble_sort(arr)
for i in range(len(arr)):
    print("%d"%arr[i])
