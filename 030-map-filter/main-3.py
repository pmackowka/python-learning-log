# map()/filter() na liście słowników - podwyżka wynagrodzeń i filtrowanie wg progu.
employees = [
    {"name": "John", "age": 28, "salary": 4000},
    {"name": "Jane", "age": 34, "salary": 5500},
]


def increase_salary(employee):
    employee["salary"] = round(employee["salary"] * 1.10, 2)
    return employee


updated_employees = list(map(increase_salary, employees))
print(updated_employees)
# [{'name': 'John', 'age': 28, 'salary': 4400.0}, {'name': 'Jane', 'age': 34, 'salary': 6050.0}]

print("-" * 30)


def filter_high_salary(employee):
    return employee["salary"] > 5000


# Zastosowanie filter na zaktualizowanej liście
high_salary_employees = list(filter(filter_high_salary, updated_employees))

# Wyświetlanie wyników
print("Updated employees with 10% salary increase:")
for emp in updated_employees:
    print(emp)

print("\nEmployees with salary greater than 5000:")
for emp in high_salary_employees:
    print(emp)

# Updated employees with 10% salary increase:
# {'name': 'John', 'age': 28, 'salary': 4400.0}
# {'name': 'Jane', 'age': 34, 'salary': 6050.0}

# Employees with salary greater than 5000:
# {'name': 'Jane', 'age': 34, 'salary': 6050.0}
