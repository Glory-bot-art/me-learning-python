class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

s1 = Student("kingzz", 20)
print(s1)  # kingzz is 20 years old