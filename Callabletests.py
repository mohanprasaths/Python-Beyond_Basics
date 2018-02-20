class CallableClass:
    def check(self):
        print("check")


def check():
    print("check")

class CallableInstanceObj:
    def __call__(self, *args, **kwargs):
        print("check")

lambdaCheck = lambda x : print("x")

print(callable(CallableClass))
print(callable(check))

instanceObj = CallableInstanceObj()
instanceObjNotwokr = CallableClass()

print(callable(instanceObj))
print(callable(instanceObjNotwokr))
print(callable(lambdaCheck))