salaries = [30000, 45000, 55000, 70000, 80000]

high_salaries = [
    salary for salary in salaries
    if salary >= 50000
]

print("High salaries:", high_salaries)