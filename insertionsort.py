def insertionsort(arr):
    
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while(j>=0 and arr[j]>key):
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key


def printarray( arr):
    
    for i in range(0,len(arr)):
        print(arr[i],end=" ")
    print(" ")

arr=[25,21,13,35,10]
insertionsort(arr)
printarray(arr)
