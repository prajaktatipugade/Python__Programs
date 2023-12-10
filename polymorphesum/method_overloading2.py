class map:
    def add(self,*args):
        sum=0
        for a in args:
            sum=sum+a
        print(sum)
obj=map()
obj.add(2,3)
obj.add(2,3,4)
