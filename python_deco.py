

# decorator take function as argument 
def transation(func):
   def wrapper():
     print("transation is start")
     func()
   return wrapper

@transation
def hello():
 print("transation is completed")
hello()



