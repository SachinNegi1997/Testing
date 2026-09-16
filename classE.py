


class Comp:
 
   def __init__(self,name,model): # when object is creating constructor is by default created 

     self.name = name           #self is reffer to obect name or byself
     self.model = model


com1 = Comp("lenovo","thinkpad")  # object is created 

print(com1.name)
print(com1.model)

com2 = Comp("dell", "latitude")
print(com2.name)
print(com2.model)

