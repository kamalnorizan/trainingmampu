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
emp1.displayEmployee()
emp1.displayCount()

emp2 = Employee("Amir", 30000)
emp2.displayEmployee()
emp2.displayCount()