Student_List = []
class Low_Student :
    school_name = "Little school"
    def __init__(self,name,id):
        self.name = name
        self.id = id
        Student_List.append(self)


    def __str__(self):
        return self.who_am_i()


    def who_am_i(self):
        return ("I am {0}".format(self.name))