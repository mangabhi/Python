#selection sort
def selection_sort(arr,n):
    for i in range(n):
        min_ind=i
        for j in range(i+1,n):
            if arr[min_ind]>arr[j]:
                min_ind=j
        
        arr[min_ind],arr[i]=arr[i],arr[min_ind]

arr=[4,1,7,9,3,2,1]
n=len(arr)
selection_sort(arr,n)
for i in range(n):
    print("%d"%arr[i])
