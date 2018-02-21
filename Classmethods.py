class Superhero:
    avengerCount = 0
    superHeroCount = 0
    def __init__(self,name,power,isAvenger):
        self.name = name
        self.power = power
        self.superHeroCounter()
        if isAvenger:
            Superhero.avengerCountAdd()

    @staticmethod
    def avengerCountAdd():
        Superhero.avengerCount += 1
        return Superhero.avengerCount


    @staticmethod
    def getAvengerGet():
        return Superhero.avengerCount

    #use classMethod if class object is needed
    @classmethod
    def superHeroCounter(cls):
        cls.superHeroCount += 1

    @classmethod
    def getSuperHeroCount(cls):
        return cls.superHeroCount


ironman = Superhero("tony" , 99 , True)
captain = Superhero("steve", 98 , True)
warlock = Superhero("adam" , 89 , False)

print(Superhero.getAvengerGet())
print(Superhero.getSuperHeroCount())
