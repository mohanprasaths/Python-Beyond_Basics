def myDecorator(f):
    c = 9
    print("I am going to add values")
    def newf(a,b,c):
        print(a,b,c)
    return newf

@myDecorator
def add(a,b):
    return a+b



add(1,2,3)

class callCount:
    def __init__(self,f):
        self.count = 0
        self.f = f


    def __call__(self, *args, **kwargs):
        self.count +=1
        self.f(*args,**kwargs)

@callCount
def sayHello():
    print("Hello")


sayHello()
sayHello()
print(sayHello.count)