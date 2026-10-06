try:
    salary = float(input("Enter salary: "))

    print("Salary:", salary)

except ValueError:
    print("Invalid input! Please enter a valid number.")