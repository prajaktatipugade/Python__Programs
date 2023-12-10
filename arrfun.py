import array as arr
a=arr.array('i',[1,2,3,4,5,6,7,8,9,9,10])
x1=arr.array('i',[1])
for i in range(0,11):
        print(a[i],end=" ")
a.append(3)
a.insert(4,7)
a.pop(3)
a.remove(8)
x=a.count(9)
print(x)
y=a.index(5)
print(y)
for i in range(0,9):
        print(a[i],end=" ")
        
        
