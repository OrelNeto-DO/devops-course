class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, i'm {self.name} and i'm {self.age} years old. my grade for the current semester is '{self.grade}'."

class Student(Person):

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def study(self, profession):
        self.profession = profession
        return f"{self.name} is studying {self.profession} classes right now"

student1 = Student("orel", 25, "A")
print(student1.introduce())
print(student1.study("python"))

student2 = Student("random", 23, "B")
print(student2.introduce())
print(student2.study("biology"))

student3 = Student("plankton", 27, "A")
print(student3.introduce())
print(student3.study("pharmacy"))

studnet4 = Student("mister crab", 47, "A")
print(studnet4.introduce())
print(studnet4.study("how to cook anything but burgers in his"))

student5 = Student("emil,", 26, "C")
print(student5.introduce())
print(student5.study("CyberSecurity"))
print(f"{student5.name} is thinking about replacing his career into {student5.study('DevOps').split('is ')[1].split(' ')[1]} engineer") #the last print statement has done with help by chat gpt. i would like to understand it more throughly.