from l_student import Low_Student

class High_Student(Low_Student) :
    school_name = "High school"

    def __str__(self):
        return self.who_am_i()

    def who_am_i(self):
        return ("I am from {0} and my name is {1}".format(self.school_name,self.name))