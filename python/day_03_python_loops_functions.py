# 1. for Loop (3 Exercises)

# Exercise 1
for numbers in range(1, 11):
    print(numbers)

# Exercise 2
fruits = ["Apple", "Mango", "Banana", "Orange", "Kiwi"]
for fruit in fruits:
    print(fruit)

# Exercise 3
sum_of_numbers = 0
for number in range(1, 101):
    sum_of_numbers+= number
print(f"Sum: {sum_of_numbers}")

# 2. while Loop (3 Exercises)

# Exercise 1
a = 1
while a <= 10:
    print(a)
    a += 1

# Exercise 2
a = 5
b = 1
while b <= 10:
    print(f"{a} x {b} = {a*b}")
    b += 1

# Exercise 3
a = 1
while a != 0:
    a = int(input("Enter a number: "))
print("Program Ended")

# 3. break (2 Exercises)

# Exercise 1 (Using while loop)
num = 0
while num <= 20:
    num += 1
    print(num)
    if num == 10:
        break
# Exercise 1 (Using for loop)
for num in range(1, 21):
    print(num)
    if num == 11:
        break

# Exercise 2
pwd = 'pwd'
while pwd != 'python123':
    pwd = input("Enter the password: ")
    if pwd == 'python123':
        print("Access Granted")
        break

# 4. continue (2 Exercises)

# Exercise 1
multiple_of_3 = []
for i in range (1, 11):
    multiple_of_3.append(3*i)

for num in range(1, 21):
    if num not in multiple_of_3:
        print(num)
        continue

# Exercise 2
for num in range(1, 21):
    if num%2 == 0:
        print(num)
        continue

# 5. Functions (3 Exercises)

# Exercise 1
def greet():
    print("Welcome to Python!")

greet()

# Exercise 2
def display_info(Name, City, Profession):
    Name = Name
    City = City
    Profession = Profession
    print(f"Name: {Name}")
    print(f"City: {City}")
    print(f"Profession: {Profession}")

display_info("Vivek", "Indore", "IT Employee")

# Exercise 3
def print_line():
    print("------------------------------")

print_line()
print_line()
print_line()
print_line()
print_line()

# 6. Function Parameters (3 Exercises)

# Exercise 1
def greet(name):
    print(f"Hello {name}")

greet("Vivek")

# Exercise 2
def add_numbers(num1, num2):
    print(num1+num2)

add_numbers(10, 20)

# Exercise 3
def employee_details(name, department):
    print(f"Employee: {name}")
    print(f"Department: {department}")

employee_details("Alich", "IT")

# 7. Return Values (3 Exercises)

# Exercise 1
def square(number):
    return number**2

result = square(6)
print(result)

# Exercise 2
def find_max(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return ("Both are equal")
    
print(find_max(25, 40))

# Exercise 3
def calculate_bonus(salary):
    if salary >= 70000:
        return (salary*20)/100
    elif salary >= 50000:
        return (salary*10)/100
    else:
        return (salary*5)/100

print(calculate_bonus(60000))

# Bonus Challenges

# Print the Fibonacci series up to 10 terms.
n = 10
a , b = 0 , 1
for _ in range(n):
    print(a, end=" ")
    a , b = b , a+b

# Check whether a number is prime.
num = int(input("Enter the number: "))
if num < 2:
    print("Not prime")
else:
    for i in range (2, int(num**0.5) + 1):
        if num % i == 0:
            print("Not prime")
            break
    else:
        print("Prime")

