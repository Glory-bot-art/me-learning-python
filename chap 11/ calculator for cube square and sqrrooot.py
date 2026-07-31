class calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        return self.n * self.n

    def cube(self):
        return self.n * self.n * self.n

    def square_root(self):
        return self.n ** 0.5


n = int(input("Enter a number: "))
c = calculator(n)
print ("in square")
print (c.square())
print ("in cube")
print(c.cube())
print ("in square root")
print(c.square_root().__round__(2))