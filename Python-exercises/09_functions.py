def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)


salaries = [50000, 60000, 70000]

average = calculate_average(salaries)

print("Average salary:", average)