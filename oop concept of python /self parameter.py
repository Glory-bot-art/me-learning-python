# class Employee:
#     def __init__(self, name, salary):
#         # We received 'name' and 'salary', but didn't glue them to 'self'!
#         print("Employee created!")

# # Create two employees
# e1 = Employee("Alice", 50000)
# e2 = Employee("Bob", 60000)

# # Now try to print their names...
# print(e1.name)

class Employee:
    def __init__(self, name, salary):
        # 'self.name' saves the 'name' input onto THIS specific employee
        self.name = name
        self.salary = salary

# Create two employees
e1 = Employee("Alice", 50000)
e2 = Employee("Bob", 60000)

# Now print their info:
print(e1.name, "makes", e1.salary)
print(e2.name, "makes", e2.salary)