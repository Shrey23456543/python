class Employee():
    def __init__(self,name,salary,department):
        self.name=name
        self.salary=salary
        self.department=department
name = input("Enter employee name: ")
department = input("Enter employee department: ")
salary=int(input("Enter employee salary:"))
emp1=Employee(name,salary,department)
new=emp1.salary/10
new_sal=emp1.salary+new

print("new salary after bonus will be:",new_sal,emp1.name,emp1.department)
