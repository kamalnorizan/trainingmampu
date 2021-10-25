class Employee:

    empCount = 0
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total employee ", Employee.empCount)

    def displayEmployee(self):
        print('Name : ', self.name, " , Salary: ", self.salary)


emp1 = Employee("Zainal", 20000)
print(emp1.name)
emp1.age = 35
if(hasattr(emp1,'age')):
    print(emp1.age)
# emp1.age = 35
# try:
#     print(emp1.age)
# except :
#     print('Error: age not found')
# else:
#     print()

# inputName = input(' Please enter the name that you want to change : ')
# emp1.name = inputName
# emp1.displayEmployee()
# emp1.displayCount()

# emp2 = Employee("Amir", 30000)
# del emp2.salary
# emp2.salary = 40000
# emp2.displayEmployee()
# emp2.displayCount()

# print(emp1.__dict__)
# print(emp1.__doc__)
# print(emp1.__module__)
# print(emp1.__class__.__name__)
