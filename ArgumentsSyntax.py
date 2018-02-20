#positional
def printArgs(a,b,c):
    print(a)
    print(b)
    print(c)

printArgs(1,2,3)

#variableargs
def printVariableArgs(a,b,*args):
    print(a)
    print(b)
    print(type(args))
    for number in (args):
        print(number)

printVariableArgs(1,2,3,4,5,6,6,77,7)

#keyVariableArgs
def printKeyVariableArgs(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(type(args))
    print(type(kwargs))

    for number in (args):
        print(number)

    for values in (kwargs):
        print("{k} is {v}".format(k = str(values),v = kwargs[values]))

printKeyVariableArgs(1,2,3,4,5,6,78,name="mohan",profession="developer")