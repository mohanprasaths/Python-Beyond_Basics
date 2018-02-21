def raiseTo(powerValue):
    def power(x):
        return pow(x,powerValue)
    return power

square = raiseTo(2)
print(square(2))

cube = raiseTo(3)
print(cube(2))