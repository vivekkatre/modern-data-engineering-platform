# 1. Opening Files (open())
# Exercise 1
open("students.txt", "w") # created file
students = open("students.txt", "r") # opened file in read mode
content = students.read()
print(content) # print file content
students.close() # closed file

# Exercise 2
students = open("students.txt", "w") # opened file in write mode
students.write("Alice\nBob\nCharlie") # written in the file
students.close() # closed file

# Exercise 3
students = open("students.txt", "a") # opened file in append mode
students.write("\nDavid\nEva") # written the new students name at the end.
print("Students are added")
students.close() # closed file

# 2. Reading Files

# Exercise 1
students = open("students.txt", "r") # opened file in read mode
content = students.read()
print(content) # print student file content
students.close() # closed file

# Exercise 2
students = open("students.txt", "r") # opened file in read mode
print(students.readline()) # print 1st line
print(students.readline()) # print 2nd line
students.close() # closed file

# Exercise 3
students = open("students.txt", "r") # opened file in read mode
lines = students.readlines() # read all lines of file
print(lines) # print all lines list
print(len(lines))
students.close() # closed file

# 3. Writing Files

# Exercise 1
file = open("employees.txt", "w") # created employees.txt file
file.write("101,Alice,IT\n102,Bob,HR\n103,Charlie,Finance") # written content in the file
file.close()

# Exercise 2
employees = [
    "104,David,IT\n",
    "105,Eva,HR\n",
    "106,Frank,Finance\n"
]

file = open("employees.txt", "w")
file.writelines(employees) # written all records using list.
file.close()

# Exercise 3
file = open("employees.txt", "w")
file.write("Department Report")
file.close()

# 4. Append Mode

# Exercise 1
file = open("employees.txt", "a")
file.write("\n107,Grace,Marketing")
file.close()

# Exercise 2
file = open("employees.txt", "a")
file.writelines([x for x in employees])
file.close()

# Exercise 3
file = open("employees.txt", "r")
content = file.read()
print(content)
file.close()

# 5. with Statement

# Exercise 1
with open("students.txt", "r") as students:
    content = students.read()

# Exercise 2
with open("courses.txt", "w") as courses:
    courses.write("Information Technology\nComputer Science\nElectronics\nRobotics\nArtifical Intelliegence")

# Exercise 3
with open("courses.txt", "r") as courses:
    content = courses.read()
    print(content)

# 6. Exception Handling

# Exercise 1
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
try:
    print(num1/num2)
except ZeroDivisionError:
    print("Can not divide by zero")

# Exercise 2
filename = input("Enter the filename: ")
try:
    with open(filename, "r") as file:
        file.read()
except FileNotFoundError:
    print("File does not exist.")

# Exercise 3
try:
    number = int(input("Enter an integer: "))
except ValueError:
    print("Wrong input given, please give correct input")

# 7. else

# Exercise 1
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
try:
    print(num1/num2)
except ZeroDivisionError:
    print("Can not divide by zero")
else:
    print("Division successful.")

# Exercise 2
filename = input("Enter the filename: ")
try:
    with open(filename, "r") as file:
        file.read()
except FileNotFoundError:
    print("File does not exist.")
else:
    print("File opened successfully.")

# 8. finally

# Exercise 1
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
try:
    print(num1/num2)
except ZeroDivisionError:
    print("Can not divide by zero")
else:
    print("Division successful.")
finally:
    print("Program finished.")

# Exercise 2
file = None

try:
    file = open("file.txt", "r")
except FileNotFoundError:
    print("File does not exist.")
finally:
    if file:
        file.close()

# 9. Raising Exceptions

# Exercise 1
def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or above.")
    
# Exercise 2
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient balance.")

# Exercise 3
def check_marks(marks):
    if marks < 0 or marks > 100:
        raise ValueError("Invalid Marks")
    else:
        print("Valid Marks")

# Mini Challenge
while True:
    print("\n=====Student File Manager=====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = int(input())

    if choice == 1:
        add_student = input("Enter Student Name: ")
        if add_student == "":
            raise ValueError("Empty Student Name")
        try:
            with open("students.txt", "a") as students:
                students.write(f"{add_student}\n")
        except FileNotFoundError:
            print("File does not exist.")
        else:
            print("Student addedd successfully.")
    
    elif choice == 2:
        try:
            with open("students.txt", "r") as students:
                content = students.read()
                print(content)
        except FileNotFoundError:
            print("File does not exist.")

    elif choice == 3:
        search_student = input("Search Student Name: ")
        if search_student == "":
            raise ValueError("Empty Student Name")      
        try:
            with open("students.txt", "r") as students:
                students_list = [students.strip() for student in students.readlines()]
                if search_student in students_list:
                    print (f"Student: {search_student}  found.")
                else:
                    print(f"Student: {search_student} doesn't exist in the file.")
        except FileNotFoundError:
            print("File does not exist.")
    
    elif choice == 4:
        break

    else:
        print("Invalid choice!")