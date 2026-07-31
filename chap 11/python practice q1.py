class programmers:
    company="microslop"
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = programmers("kingzz", 20)
print(p1.name)
print(p1.age)
print (programmers.company)
print("------------")
p2=programmers("not kingzz", 2020)
print(p2.name)
print(p2.age)
print(programmers.company)