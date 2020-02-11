#Array rotation
def abc(arr,k,n):
    p=k%n
    s=""
    for i in range(n):
        print(str(arr[(p+i)%n]))
    print
    return

arr=[3,2,6,11,9,4,3]
k=2
n=len(arr)
print(abc(arr,k,n))
