from functools import reduce
class InfinityStones:
    def __init__(self,name,power,value):
        self.name = name
        self.power = power
        self.value = value


    def __str__(self):
        return  ("This is {infinitystone} infinity stone and it has {power}".format(infinitystone=self.name,power=self.power))

    def __repr__(self):
        return ("THe value of name is {name} and power is {power}".format(name=self.name,power=self.power))

    @staticmethod
    def printWithValues(obj):
        print(obj.name , obj.power)
        return obj.name

mindstone = InfinityStones("mindstone", "control people",80)
tesseract = InfinityStones("tesseract" , "Opnes portal",89)
time = InfinityStones("timestone","time travel",99)
power = InfinityStones("power" ,"infinite power",100)

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


#Filter
def filter_my_infy(obj):
    if((obj.value)>= 90):
        return True
    return False


print("My powers stones are")
power_infinity_stones = filter(filter_my_infy,gem_list)
for o in map(InfinityStones.printWithValues,power_infinity_stones):
    print(o)

#reduce
def my_infy_power_reducer(cumu_value , obj):
    return cumu_value + obj.value

cumuValue = reduce(my_infy_power_reducer,gem_list,500)
print(cumuValue)

dict_list= []
dict_list.append(({i:i*2 for i in range(10)}))
print(dict_list)