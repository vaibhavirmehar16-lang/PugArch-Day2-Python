class Employee:
    def __init__(self, employee_id, name, department, salary, email):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.salary = salary
        self.email = email

    def to_dict(self):
        return {
            "employee_id": self.employee_id,
            "name": self.name,
            "department": self.department,
            "salary": self.salary,
            "email": self.email
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["employee_id"],
            data["name"],
            data["department"],
            data["salary"],
            data["email"]
        )

    def __str__(self):
        return (
            f"ID: {self.employee_id} | "
            f"Name: {self.name} | "
            f"Department: {self.department} | "
            f"Salary: {self.salary} | "
            f"Email: {self.email}"
        )