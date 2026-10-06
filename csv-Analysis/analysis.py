import csv


FILE_PATH = "data/employees.csv"


def load_data(file_path):
    """Load employee records from CSV."""

    employees = []

    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["employee_id"] = int(row["employee_id"])
            row["salary"] = float(row["salary"])
            row["experience"] = float(row["experience"])

            employees.append(row)

    return employees


def calculate_numeric_statistics(employees, column):
    """Calculate average, minimum and maximum."""

    values = [employee[column] for employee in employees]

    return {
        "average": sum(values) / len(values),
        "minimum": min(values),
        "maximum": max(values)
    }


def find_missing_values(employees):
    """Find missing values for each column."""

    if not employees:
        return {}

    columns = employees[0].keys()

    missing = {}

    for column in columns:
        missing[column] = sum(
            1
            for employee in employees
            if employee[column] == ""
        )

    return missing


def find_duplicates(employees):
    """Count duplicate records."""

    unique_records = set()
    duplicate_count = 0

    for employee in employees:
        record = tuple(employee.items())

        if record in unique_records:
            duplicate_count += 1
        else:
            unique_records.add(record)

    return duplicate_count


def department_statistics(employees):
    """Calculate department-wise statistics."""

    departments = {}

    for employee in employees:

        department = employee["department"]

        if department not in departments:
            departments[department] = []

        departments[department].append(employee)

    statistics = {}

    for department, department_employees in departments.items():

        salaries = [
            employee["salary"]
            for employee in department_employees
        ]

        statistics[department] = {
            "count": len(department_employees),
            "average_salary": sum(salaries) / len(salaries),
            "minimum_salary": min(salaries),
            "maximum_salary": max(salaries)
        }

    return statistics


def display_report(employees):
    """Display complete analysis report."""

    print("\n" + "=" * 60)
    print("              EMPLOYEE CSV ANALYSIS")
    print("=" * 60)

    # Record count
    print("\nTotal Records:", len(employees))

    # Missing values
    print("\nMissing Values")
    print("-" * 30)

    missing = find_missing_values(employees)

    for column, count in missing.items():
        print(f"{column}: {count}")

    # Duplicate analysis
    duplicates = find_duplicates(employees)

    print("\nDuplicate Records:", duplicates)

    # Salary statistics
    salary_stats = calculate_numeric_statistics(
        employees,
        "salary"
    )

    print("\nSalary Statistics")
    print("-" * 30)

    print(
        "Average Salary:",
        round(salary_stats["average"], 2)
    )

    print(
        "Minimum Salary:",
        salary_stats["minimum"]
    )

    print(
        "Maximum Salary:",
        salary_stats["maximum"]
    )

    # Experience statistics
    experience_stats = calculate_numeric_statistics(
        employees,
        "experience"
    )

    print("\nExperience Statistics")
    print("-" * 30)

    print(
        "Average Experience:",
        round(experience_stats["average"], 2),
        "years"
    )

    print(
        "Minimum Experience:",
        experience_stats["minimum"],
        "years"
    )

    print(
        "Maximum Experience:",
        experience_stats["maximum"],
        "years"
    )

    # Department statistics
    print("\nDepartment Statistics")
    print("-" * 30)

    department_data = department_statistics(employees)

    for department, stats in department_data.items():

        print("\nDepartment:", department)
        print("Employees:", stats["count"])

        print(
            "Average Salary:",
            round(stats["average_salary"], 2)
        )

        print(
            "Minimum Salary:",
            stats["minimum_salary"]
        )

        print(
            "Maximum Salary:",
            stats["maximum_salary"]
        )


def main():
    try:

        employees = load_data(FILE_PATH)

        if not employees:
            print("No employee records found.")
            return

        display_report(employees)

    except FileNotFoundError:
        print("Error: CSV file not found.")

    except ValueError as error:
        print("Error while processing data:", error)

    except Exception as error:
        print("Unexpected error:", error)


if __name__ == "__main__":
    main()