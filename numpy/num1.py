import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)
arr2=np.array([[1,2,3,4,5],[3,4,5,6,7]])
print(arr2)
print(arr2.ndim) #arraydimension
arr3=np.array([1,2,3,4],ndmin=5) #
print(arr3)
print('number of dimension:',arr3.ndim)
print(arr[2])
print(arr[2]+arr[3]) ##addition of array
print("2 nd elemnt on 1 row:",arr2[1,2])
print("2 nd elemnt on 1 row:",arr2[1,2])
print('Last element from 2nd dim: ', arr2[1, -1])
print(arr[1:2])
print(arr[1:2])
print(arr.dtype)
print(arr.astype(int))
print(arr.shape)
newarr = arr.reshape(4, 3)
for x in arr2:
  for y in x:
    print(y)
for x in arr:
  for y in x:
    print(y)
arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr))
arr = np.array([True, False, True])

print(np.sort(arr))
