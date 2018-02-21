import functools
def myDecorator(f):
    c = 9
    print("I am going to add values")
    @functools.wraps(f)
    def newf(a,b,c):
        print(a,b,c)
    return newf

@myDecorator
def add(a,b):
    "I add numbers"
    return a+b



add(1,2,3)
print(add.__name__)
print(add.__doc__)

class callCount:
    def __init__(self,f):
        "I count function calls"
        self.count = 0
        self.f = f

    def __call__(self, *args, **kwargs):
        "I count function calls"

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
    "Tracer"
    def __init__(self):
        self.enabled =True

    def __call__(self,f ):
        def wrapper(*args,**kwargs):
            if self.enabled:
                print("Calling function and inside tracer")
            f(*args,**kwargs)
        return wrapper

tracer = Tracer()

@callCount
@tracer
def sayHi(name):
    "I say hi with name"
    print("Hello {name}".format(name=name))

sayHi("mohan")
tracer.enabled = False
sayHi("batman")
sayHi("batman")
print(sayHi.count)
