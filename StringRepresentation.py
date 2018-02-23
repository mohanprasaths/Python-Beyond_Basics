class InfinityStones:
    def __init__(self,name,power):
        self.name = name
        self.power = power


    def __str__(self):
        return  ("This is {infinitystone} infinity stone and it has {power}".format(infinitystone=self.name,power=self.power))

    def __repr__(self):
        return ("THe value of name is {name} and power is {power}".format(name=self.name,power=self.power))

    @staticmethod
    def printWithValues(obj):
        print(obj.name , obj.power)
        return obj.name

mindstone = InfinityStones("mindstone", "control people")
tesseract = InfinityStones("tesseract" , "Opnes portal")
time = InfinityStones("timestone","time travel")
power = InfinityStones("power" ,"infinite power")

gem_list = []
gem_list.append(mindstone)
gem_list.append(tesseract)
gem_list.append(time)
gem_list.append(power)

print(str(mindstone))
print(str(tesseract))
print(repr(mindstone))
print(repr(tesseract))


map_obj = map(InfinityStones.printWithValues,gem_list)
(next(map_obj))
(next(map_obj))

for o in map(InfinityStones.printWithValues,gem_list):
    print(o)