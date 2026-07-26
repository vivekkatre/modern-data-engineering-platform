# Employees
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

# All function definitions

# display_all_employees()
def display_all_employees():
    for employee in employees:
        print(f"ID: {employee['id']}")
        print(f"Name: {employee['name']}")
        print(f"Department: {employee['department']}")
        print(f"Salary: {employee['salary']}")
        print("-" * 30)

# filter_by_department()
def filter_by_department(department):
    for employee in employees:
        if employee['department'].lower() == department.lower():
            print(employee['name'])

# find_highest_salary()
def find_highest_salary():
    highest_salary_employee = employees[0]
    for employee in employees:
        if highest_salary_employee['salary'] < employee["salary"]:
            highest_salary_employee = employee
    print(f"Highest Salary Employee: {highest_salary_employee['name']}")
    print(f"Highest Salary: {highest_salary_employee['salary']}")

# calculate_average_salary()
def calculate_average_salary():
    total_salary = 0
    for employee in employees:
        total_salary += employee["salary"]
    average_salary = total_salary/len(employees)
    print(f"Average Salary: {average_salary}")

# search_employee(name)
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

# Create count_employees() to display the total number of employees.
def count_employees():
    print(f"Total Employees: {len(employees)}")

# Create find_lowest_salary().
def find_lowest_salary():
    lowest_salary = employees[0]['salary']
    for employee in employees:
        if lowest_salary > employee['salary']:
            lowest_salary = employee["salary"]
    print(f"Lowest Salary: {lowest_salary}")

# Create employees_above_salary(min_salary).
def employees_above_salary(min_salary):
    for employee in employees:
        if employee["salary"] > min_salary:
            print(f"Employees whose salary above {min_salary} are: {employee['name']}")

# Add Employee
def add_employee():
    employee_id = int(input('Enter ID: '))
    name = input('Enter Name: ')
    department = input('Enter Department: ')
    salary = int(input('Enter Salary: '))
    new_emp = {'id' : employee_id, 'name' : name, 'department' : department, 'salary' : salary}
    employees.append(new_emp)
    print("\nEmployee added successfully.")

# Update Employee Salary
def update_employee_salary(employee_id, new_salary):
    for employee in employees:
        if employee_id == employee['id']:
            old_salary = employee['salary']
            employee['salary'] = new_salary
            print("Employee Details")
            print('-' * 10)
            print(f"Employee ID: {employee['id']}")
            print(f"Employee Name: {employee['name']}")
            print(f"Employee Department: {employee['department']}")
            print(f"Employee Old Salary: {old_salary}")
            print(f"Employee New Salary: {employee['salary']}")
            break
    else:
        print("Employee not found.")

# Delete Employee
def delete_employee(employee_id):
    for employee in employees:
        if employee['id'] == employee_id:
            employees.remove(employee)
            print("Employee deleted successfully.")
            return
    else:
        print("Employee not found.")

# Search Employee by ID
def search_employee_by_id(employee_id):
    for employee in employees:
        if employee['id'] == employee_id:
            print(f"ID: {employee['id']}")
            print(f"Name: {employee['name']}")
            print(f"Department: {employee['department']}")
            print(f"Salary: {employee['salary']}")
            break
    else:
        print("Employee not found.")

# Display Department Summary
def display_department_summary():
    department_summary = {}

    for employee in employees:
        department = employee["department"]

        if department in department_summary:
            department_summary[department] += 1
        else:
            department_summary[department] = 1

    print("\nDepartment Summary")
    print("-" * 20)

    for department, count in department_summary.items():
        print(f"{department}: {count}")

# Main Program

display_all_employees()

department = input("Enter department: ")
filter_by_department(department)

find_highest_salary()  

calculate_average_salary()

search_name = input("Enter employee name: ")
search_employee(search_name)

count_employees()

find_lowest_salary()

employees_above_salary(60000)

add_employee()

employee_id = int(input("Enter Employee ID to update Salary: "))
new_salary = int(input("Enter new salary: "))
update_employee_salary(employee_id, new_salary)

employee_id = int(input("Enter Employee ID to delete: "))
delete_employee(employee_id)

employee_id = int(input("Enter Employee ID you want to search: "))
search_employee_by_id(employee_id)

display_department_summary()



