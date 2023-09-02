class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print('name :',self.name)
        print('age :',self.age)
class student(person):
    def __init__(self,rollno,name,age):
        self.rollno=rollno
        person.__init__(self,name,age)
        
    def display(self):
        print('rollno :',self.rollno)
        person.display(self)
        
s1=student(10,'arul',21)
print('student details : ')
s1.display()
