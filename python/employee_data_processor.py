employees = [
    {
        "id": 101,
        "name": "Alice",
        "department": "IT",
        "salary": 65000
    },
    {
        "id": 102,
        "name": "Bob",
        "department": "HR",
        "salary": 50000
    },
    {
        "id": 103,
        "name": "Charlie",
        "department": "Finance",
        "salary": 72000
    },
    {
        "id": 104,
        "name": "David",
        "department": "IT",
        "salary": 68000
    },
    {
        "id": 105,
        "name": "Eva",
        "department": "HR",
        "salary": 55000
    }
]

# Task 1 – Print All Employees
for i in employees:
    print(f"Employee ID: {i['id']}\nName: {i['name']}\nDepartment: {i['department']}\nSalary: {i['salary']}")

# Task 2 – Filter Employees by Department
dept = input("Enter department:")
for i in employees:
    if i['department'].lower() == dept.lower():
        print(i['name'])

# Task 3 – Find the Highest Salary
highest_salary = employees[0]
for employee in employees:
    if employee['salary'] > highest_salary['salary']:
        highest_salary = employee

print(f"Highest Salary Employee\n{highest_salary['name']}\n{highest_salary['salary']}")

# Task 4 – Calculate the Average Salary
total_salary = 0
salary_list = []
for employee in employees:
    total_salary = total_salary + employee["salary"]
count = len(employees)
print(f"Average Salary: {total_salary/count}")

