class Student:
    age =0
    marks =0

    def __init__(self,name,roll):
        self.name = name
        self.roll = roll

    def setAge(self,age):
        self.age = age

    def setMarks(self,marks):
        self.marks = marks

    def Display(self):
        return "name:{} - roll:{} - age:{} - marks{}.".format(self.name, self.roll, self.age, self.marks)

s1=Student("mithun",50)

Student.setAge(s1,20)
print(s1.name,s1.roll)
print(s1.age)

Student.setMarks(s1,200)
print(s1.marks)

print(Student.Display(s1))