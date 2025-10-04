a=10
b=20
def add(x,y):
    c=x+y
    return c
print(add(a,b))
print(add(100,200))
class Person:
    def  __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"Name:{self.name},Age:{self.age}")    
per=Person("Alice",30)
per.info()