def validate_name(name):
    if not name.strip():
        raise ValueError("Name cannot be empty.")

    if not name.replace(" ", "").isalpha():
        raise ValueError("Name should contain only letters.")

    return name.strip()


def validate_department(department):
    if not department.strip():
        raise ValueError("Department cannot be empty.")

    return department.strip()


def validate_salary(salary):
    try:
        salary = float(salary)
    except ValueError:
        raise ValueError("Salary must be a valid number.")

    if salary <= 0:
        raise ValueError("Salary must be greater than zero.")

    return salary


def validate_email(email):
    email = email.strip()

    if "@" not in email or "." not in email:
        raise ValueError("Invalid email address.")

    return email