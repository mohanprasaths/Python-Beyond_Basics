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