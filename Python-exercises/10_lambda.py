employees = [
    {"name": "Rahul", "salary": 55000},
    {"name": "Priya", "salary": 70000},
    {"name": "Amit", "salary": 45000}
]

sorted_employees = sorted(
    employees,
    key=lambda employee: employee["salary"]
)

for employee in sorted_employees:
    print(employee["name"], employee["salary"])