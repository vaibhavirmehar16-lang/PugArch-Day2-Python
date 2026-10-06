import json
from pathlib import Path

from employee import Employee


class EmployeeManager:

    def __init__(self, file_path):
        self.file_path = Path(file_path)
        self.employees = []
        self.load_data()

    def load_data(self):
        try:
            if not self.file_path.exists():
                self.file_path.parent.mkdir(parents=True, exist_ok=True)
                self.save_data()
                return

            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            self.employees = [
                Employee.from_dict(employee)
                for employee in data
            ]

        except json.JSONDecodeError:
            print("Error: JSON file contains invalid data.")
            self.employees = []

    def save_data(self):
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(
                [employee.to_dict() for employee in self.employees],
                file,
                indent=4
            )

    def add_employee(self, employee):
        for existing in self.employees:
            if existing.employee_id == employee.employee_id:
                raise ValueError("Employee ID already exists.")

        self.employees.append(employee)
        self.save_data()

    def get_all(self):
        return self.employees