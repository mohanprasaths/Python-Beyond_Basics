class InfinityStones:
    def __init__(self,name,power):
        self.name = name
        self.power = power


    def __str__(self):
        return  ("This is {infinitystone} infinity stone and it has {power}".format(infinitystone=self.name,power=self.power))

    def __repr__(self):
        return ("THe value of name is {name} and power is {power}".format(name=self.name,power=self.power))

mindstone = InfinityStones("mindstone", "control people")
tesseract = InfinityStones("tesseract" , "Opnes portal")

print(str(mindstone))
print(str(tesseract))
print(repr(mindstone))
print(repr(tesseract))
