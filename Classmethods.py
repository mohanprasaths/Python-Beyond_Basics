class Superhero:
    avengerCount = 0
    superHeroCount = 0
    def __init__(self,name,power,isAvenger,topClass):
        self.name = name
        self.power = power
        self._superHeroCounter()
        if isAvenger:
            Superhero._avengerCountAdd()
        self.topClass = topClass

    @staticmethod
    def _avengerCountAdd():
        Superhero.avengerCount += 1
        return Superhero.avengerCount


    @staticmethod
    def _getAvengerGet():
        return Superhero.avengerCount

    #use classMethod if class object is needed
    @classmethod
    def _superHeroCounter(cls):
        cls.superHeroCount += 1

    @classmethod
    def _getSuperHeroCount(cls):
        return cls.superHeroCount

    @property
    def topClass(self):
        return self._topClass

    @topClass.setter
    def topClass(self,isTopClass):
        if isTopClass and self.power > 90:
            self._topClass = True
        else:
            raise Exception("Not enough power for {name}".format(name= self.name))

try:
    ironman = Superhero("tony" , 99 , True,True)
    captain = Superhero("steve", 98 , True,True)
    blackwidow = Superhero('Natasa',65 , True, True)
    warlock = Superhero("adam" , 89 , False,True)
    blackwidow = Superhero('Natasa',65 , True, True)
except Exception as e:
    print(e)

print(Superhero._getAvengerGet())
print(Superhero._getSuperHeroCount())
