# 1. Classes & Objects

# Exercise 1
class Student:
    pass

student1 = Student()
student2 = Student()

# Exercise 2
class Car:
    pass

car1 = Car()
car2 = Car()
car3 = Car()

# Exercise 3
class Book:
    pass

book1 = Book()
book2 = Book()

# 2. Attributes

# Excercise 1
student1.name = "Vivek"
student1.age = 28
student1.course = "Data Engineering"

print(student1.name)
print(student1.age)
print(student1.course)

# Exercise 2
car1.brand = "Audi"
car1.model = "A6"
car1.year = "2018"

print(car1.brand)
print(car1.model)
print(car1.year)

# Exercise 3
class Employee:
    pass
employee1 = Employee()
employee2 = Employee()

employee1.id = 7
employee1.name = "Harry"
employee1.salary = 70000

employee2.id = 12
employee2.name = "Ron"
employee2.salary = 70000

print(employee1.id)
print(employee1.name)
print(employee1.salary)
print(employee2.id)
print(employee2.name)
print(employee2.salary)


# 3. Methods

# Exercise 1
class Students:
    def display(self):
        print("Harry")
        print("Ron")
        print("Hermoinee")

student = Students()
student.display()

# Exercise 2
class Calculator:
    def add(self):
        pass
    def substract(self):
        pass

calculator = Calculator()
calculator.add()
calculator.substract()

# Exercise 3
class Rectangle:
    def calculate_area(self):
        print("area")

rectangle = Rectangle()
rectangle.calculate_area()

# 4. Constructors (__init__)

# Exercise 1
class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

student1 = Student("Vivek", 28, "Data Engineering")
student2 = Student("Harry", 30, "Defence Against Dark Arts")

# Exercise 2
class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary
        print(self.id)
        print(self.name)
        print(self.salary)

employee = Employee(27, "Vivek", 120000)

# Exercise 3:
class Laptop:
    def __init__(self, brand, ram, price):
        self.brand = "HP"
        self.ram = "16 GB"
        self.price = 70000

        print(self.brand)
        print(self.ram)
        print(self.price)

laptop = Laptop()

# 5. Instance vs Class Variables
# Exercise 1
class Student:
    school = "ABC School"
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Harry", 17)

student2 = Student("Ron", 17)

student3 = Student("Hermoinee", 17)

# Exercise 2
class Car:
    wheels = 4
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

car1 = Car("Ferari", "Red")

car2 = Car("BMW", "Black")

# Exercise 3
class Employee:
    company = "XYZ Pvt Ltd"
    def __init__(self, id, name):
        self.id = id
        self.name = name

employee = Employee(27, "Joel")


# 6. Encapsulation (Basic)

# Exercise 1
class BankAccount:
    def __init__ (self, balance):
        self._balance = balance

    def deposit (self, add_balance):
        self._balance += add_balance

    def withdra1 (self, minus_balace):
        self._balance -= minus_balace
    
    def display_balance(self, balance):
        print(balance)

# Exercise 2:
class Student:
    def __init__ (self, marks):
        self._marks = marks
    
    def update_marks (self, change_marks):
        self._marks = change_marks

    def display_marks (self, marks):
        print(marks)

class Employee:
    def __init__(self, salary):
        self._salary = salary
    
    def increase_salary(self, amount):
        self._salary += amount

    def display_salary(self, salary):
        print(salary)
