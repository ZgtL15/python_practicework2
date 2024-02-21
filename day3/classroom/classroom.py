##add Person
class Person:
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname
    def getfullname(self):
        return f"{self.firstname} {self.lastname}"


##add Student
class Student(Person):
    def __init__(self,firstname,lastname,subject_area):
        super().__init__(firstname,lastname)
        self.subject_area=subject_area
    def printNameSubject(self):
        print(f"{self.getfullname()}, {self.subject_area}")

##add Teacher
class Teacher(Person):
    def __init__(self, firstname, lastname, course):
      Person.__init__(self, firstname, lastname)
      self.course = course

    def printTeacherCourse(self):
        return(self.firstname, self.lastname, self.course)


