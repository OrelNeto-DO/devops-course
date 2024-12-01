class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, i'm {self.name} and i'm {self.age} years old"

class Student(Person):

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def study(self, proffesion):
        return f"{self.name} is studying python classes right now"
        self.profession = profession

Student("orel", 25).introduce("orel", 25).study("python")
        