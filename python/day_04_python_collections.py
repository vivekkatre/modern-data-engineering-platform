# 1. Lists

# Exercise 1
pro_lang = ["Python", "Java", "C++", "R", "Scala"]
print(pro_lang)
print(pro_lang[0])
print(pro_lang[-1])

# Exercise 2
emp_salary = [45000, 50000, 38000, 74000, 90000, 55000]
Salary1 = emp_salary[0]
Total_salary = 0

for salary in emp_salary: #Highest Salary
    if Salary1 < salary:
        Salary1 = salary
print(f"Highest Salary: {Salary1}")

for salary in emp_salary: # Lowest Salary
    if Salary1 > salary: 
        Salary1 = salary
print(f"Lowest Salary: {Salary1}")

for salary in emp_salary: # Total Salary
    Total_salary += salary 
print(f"Total Salary: {Total_salary}")


# Exercise 3
List1 = []
List1.append(45)
List1.append(25)
List1.append(57)
List1.append(36)
List1.append(93)
List1.remove(93)
List1.sort()
print(List1)

# 2. Tuples
# Exercise 1
emp_id = (1001, "Vivek", "IT")
print(emp_id[0])
print(emp_id[1])
print(emp_id[-1])

# Exercise 2
weekdays = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
print(weekdays[0])
print(weekdays[-1])
print(f"Total number of days: {len(weekdays)}")

# Exercise 3
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = tuple1 + tuple2
print(tuple3)

# 3. Sets
# Exercise 1
dept_names = {"IT", "HR", "Finance", "IT", "HR"}
print(dept_names)
# Observation: Set treat repeted values as sigle value and does not print duplicates.

# Exercise 2
A = {1,2,3,4}
B = {3,4,5,6}
print(A | B) # Union
print(A & B) # Intersection
print(A - B) # Difference
print(A ^ B) # Symetric Difference

# Exercise 3
emp_ids = {1001, 1002, 1003, 1004, 1005, 1006, 1007} # Create a set of employee IDs
emp_ids.add(1008) # Add one ID
emp_ids.remove(1007) # Remove one ID
# Check whether a specific ID exists
search_id = int(input("Enter Employees ID: "))
for id in emp_ids:
    if id == search_id:
        print(f"{search_id} exist")
        break
else:
    print(f"{search_id} doesn't exist")

# 4. Dictionaries
# Exercise 1
emp_1 = {"id": 1001, "name": "Vivek", "department": "IT", "salary": 100000}
print(emp_1['id'])
print(emp_1['name'])
print(emp_1['department'])
print(emp_1['salary'])

# Exercise 2
emp_1['salary'] = 120000
print(emp_1['salary'])
emp_1['experience'] = 4
print(emp_1['experience'])
print(emp_1)

# Exercise 3
result = {
    "Alice":85,
    "Bob":92,
    "Charlie":78
}

mark1 = list(result.values())[0]

for mark in result.values():
    if mark1 < mark:
        mark1 = mark
print(f"Highest marks: {mark1}")

for mark in result.values():
    if mark1 > mark:
        mark1 = mark
print(f"Lowest marks: {mark1}")

Total_marks = 0
for mark in result.values():
    Total_marks += mark
print(f"Average marks: {Total_marks/len(result)}")

# 5. List Methods
numbers = [15, 5, 20, 10]

# Exercise 1
numbers.append(54)
print(numbers)
numbers.insert(0, 45)
print(numbers)

# Exercise 2
numbers.remove(20)
print(numbers)
numbers.pop(-1)
print(numbers)

# Exercise 3
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print(numbers.count(5))
print(numbers.index(45))

# 6. Dictionary Methods
employee = {
    "id":101,
    "name":"Alice",
    "department":"IT",
    "salary":65000
}

# Exercise 1
print(employee.keys()) # returns the keys of dictionary
print(employee.values()) # returns the values of dictionary
print(employee.items()) # returns all key, value pair of dictionary

# Exercise 2
print(employee.get("name")) # return the value for the respective key in .get()
employee.update(name = 'Vivek') # update the value for repective key in .update()
print(employee['name'])

# Exercise 3
employee.pop('name') # delete the key : value pair in dictionary for repective key in .pop()
print(employee)
employee.popitem() # delete the last key : value pair in dictionary
print(employee)


# 7. List Comprehension (Basic)

# Exercise 1
numbers = [x for x in range(1, 11)]
print(numbers)

# Exercise 2
squares = [x**2 for x in range(1, 11)]
print(squares)

# Exercise 3
even_numbers = [x for x in range(1, 21) if x%2 == 0]
print(even_numbers)

# Bonus Challenge
employees = [
    {"id":101,"name":"Alice","salary":65000},
    {"id":102,"name":"Bob","salary":50000},
    {"id":103,"name":"Charlie","salary":72000}
]

# Print all employee names.
for employee in employees:
    print(employee['name'])

# Find the highest salary.
salary1 = employees[0]['salary']
salary_list = []
for employee in employees:
    salary_list.append(employee["salary"])
    for salary in salary_list:
        if salary1 < salary:
            salary1 = salary
print(f"Highest Salary: {salary1}")

# Find the average salary.
Total_salary = 0
for employee in employees:
    Total_salary += employee['salary']
print(f"Avegare Salary: {Total_salary/len(employees)}")

# Print employees earning more than 60000.
salary1 = 60000
salary_list = []
for employee in employees:
    salary_list.append(employee["salary"])
    for salary in salary_list:
        if salary1 < salary:
            salary1 = salary
            print(f"Employee earn more than 6000: {employee['name']}")

# Create a new list containing only employee names using list comprehension.
new_list = [emp['name'] for emp in employees]
print(new_list)