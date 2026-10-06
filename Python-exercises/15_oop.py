class Employee:

    def __init__(self, employee_id, name, salary):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary

    def display(self):
        print("ID:", self.employee_id)
        print("Name:", self.name)
        print("Salary:", self.salary)


employee = Employee(101, "Rahul", 55000)

employee.display()