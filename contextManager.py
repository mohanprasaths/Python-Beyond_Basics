class Context_Manager_Custom:
    def __enter__(self):
        self.numbers = [1,2,3,4,5,6]
        return  self.numbers


    def __exit__(self, exc_type, exc_val, exc_tb):
        print("empty it")

with Context_Manager_Custom() as self:
    print(self)



with Context_Manager_Custom() as x:
    print(x)
