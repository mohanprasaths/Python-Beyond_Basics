class Animals:
    def print_me(self):
        print("I am animal")

    def __init__(self,name,weight):
        self.name = name
        self.weight = weight
        print("name is {0} and weight is {1}".format(name,weight))
