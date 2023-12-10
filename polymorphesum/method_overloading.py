from multipledispatch import dispatch
class map:
    @dispatch(int,int)
    def add(self,num1,num2):
        print("Sum:",num1+num2)
        
    @dispatch(float)
    def add(self,num1):
        print(num1/2)
        
obj=map()
obj.add(2,3)
obj.add(2.4)
