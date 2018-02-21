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

#Instance as decorator
class Tracer:
    def __init__(self):
        self.enabled =True

    def __call__(self,f ):
        def wrapper(*args,**kwargs):
            if self.enabled:
                print("Calling function and inside tracer")
            f(*args,**kwargs)
        return wrapper

tracer = Tracer()

@tracer
def sayHi(name):
    print("Hello {name}".format(name=name))

sayHi("mohan")
tracer.enabled = False
sayHi("batman")