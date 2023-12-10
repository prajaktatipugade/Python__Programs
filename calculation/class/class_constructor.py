class  car:
    category="suv"
    def __init_(self, modelname, year):
        self.modelname=modelname
        self.year=year
    def  display(self):
        print(self.modelname,self.year)
c1=car("Nexon",2)        
print(c1.category)
c1.display()
