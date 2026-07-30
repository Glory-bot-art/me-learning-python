class employee:
    name="kingzz"
    age=20
    salary=10000

l=employee()
print(l.name)
print(l.age)
print(l.salary)

print("---------------")
k=employee()
k.name="Abc"#//This is an instance attrible which gets priority//
print(k.name)
print(k.age)
print(k.salary)


# if there is no instance attribute than python will choose the default 
# or main class attribute
print("---------------")
gg=employee()
print(gg.name)