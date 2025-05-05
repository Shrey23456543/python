#oops concept

class Student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade

    def ShowInfo(self):
        print("Your name is",self.name,"and you got grade as",self.grade)
s1=Student("Shreyash","A grade")
s1.ShowInfo()
        

