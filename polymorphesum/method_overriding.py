class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class car(Vehicle):
    pass
        
class boat(Vehicle):
    def move(self):
        print("Sail!")

class plane(Vehicle):
    def move(self):
        print("fly!")

c=car("creta",123)
b=boat("Ibiza", "Touring 20")
p=plane("india",124)
for i in (c,b,p):
    print("brand:",i.brand,",","model:",i.model)
    i.move()
    
