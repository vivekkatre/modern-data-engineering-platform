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

# 1. display_all_employees()
def display_all_employees():
    for employee in employees:
        print(f"ID: {employee['id']}")
        print(f"Name: {employee['name']}")
        print(f"Department: {employee['department']}")
        print(f"Salary: {employee['salary']}")
        print("-" * 30)

# 2. filter_by_department()
def filter_by_department(department):
    for employee in employees:
        if employee['department'].lower() == department.lower():
            print(employee['name'])

# 3. find_highest_salary()
def find_highest_salary():
    highest_salary_employee = employees[0]
    for employee in employees:
        if highest_salary_employee['salary'] < employee["salary"]:
            highest_salary_employee = employee
    print(f"Highest Salary Employee: {highest_salary_employee['name']}")
    print(f"Highest Salary: {highest_salary_employee['salary']}")

# 4. calculate_average_salary()
def calculate_average_salary():
    total_salary = 0
    for employee in employees:
        total_salary += employee["salary"]
    average_salary = total_salary/len(employees)
    print(f"Average Salary: {average_salary}")

# 5. search_employee(name)
def search_employee(search_name):
    for employee in employees:
        if search_name.lower() == employee['name'].lower():
            print("Employee found")
            print(f"ID: {employee['id']}")
            print(f"Name: {employee['name']}")
            print(f"Department: {employee['department']}")
            print(f"Salary: {employee['salary']}")
            break
    else:
        print("Employee not found.")

while True:
    print("\n===== Employee Management System =====")
    print("1. View Employees")
    print("2. Search Employee")
    print("3. Filter by Department")
    print("4. Highest Salary")
    print("5. Average Salary")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_all_employees()

    elif choice == "2":
        name = input("Enter employee name: ")
        search_employee(name)

    elif choice == "3":
        department = input("Enter department: ")
        filter_by_department(department)

    elif choice == "4":
        find_highest_salary()

    elif choice == "5":
        calculate_average_salary()

    elif choice == "6":
        print("Thank you! Exiting...")
        break

    else:
        print("Invalid choice! Please try again.")
