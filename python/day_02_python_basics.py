# 1. Variables (3 Programs)

# Exercise 1
Name = "Vivek"
Age = 28
City = "Indore" 
print(Name)
print(Age)
print(City)

# Exercise 2
num1 = 2
num2 = 4
print(num1)
print(num2)
print(num1+num2)

# Exercise 3
Company = "TCS Ltd"
Experience = "4 Years"
print(f"Company: {Company}")
print(f"Experience: {Experience}")

# 2. Data Types (3 Programs)

# Exercise 1
A = 23
B = 12.5
C = "Hello"
D = True
print(A, type(A))
print(B, type(B))
print(C, type(C))
print(D, type(D))

# Exercise 2
fruits = ['Mango', 'Orange', 'Kiwi', 'Waterlemon', 'Banana']
print(fruits)
print(fruits[0])
print(fruits[-1])

# Exercise 3
employee = {
    "name": "John",
    "age": 30,
    "city": "Pune"
}
print(employee["name"])
print(employee["age"])
print(employee["city"])

# 3. Type Conversion (3 Programs)

# Exercise 1
a = "100"
print(int(a)+50)

# Exercise 2
b = 25
convert_b_to_float = float(b)
print(convert_b_to_float, type(convert_b_to_float))

# Exercise 3
c = 3.99
convert_c_to_int = int(c)
print(convert_c_to_int)

# 4. Operators (3 Programs)

# Exercise 1
num1 = 4
num2 = 2
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)

# Exercise 2
print(num1%num2)
print(num1//num2)
print(num1**num2)

# Exercise 3
print(10 > 5)
print(10 == 5)
print(10 != 5)

# 5. Input & Output (3 Programs)

# Exercise 1
Name = input("Enter your name")
print(f"Hello, {Name}")

# Exercise 2
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
print(f"Total is {num1+num2}")

# Exercise 3
Age = input("Enter your age:")
print(f"You are {Age} years old.")

# 6. Conditional Statements (3 Programs)

# Exercise 1
number = int(input("Enter your number:"))
if number>0:
    print("This number is positive")
elif number==0:
    print("This number is zero")
else:
    print("This number is Negative")

# Exercise 2
marks = int(input("Enter your marks:"))
if marks>=90:
    print("A")
elif marks>=75:
    print("B")
elif marks>=60:
    print("C")
else:
    print("Fail")

# Exercise 3
Age = int(input("Enter your age: "))
if Age>=18:
    print("Eligible to vote")
else:
    print("Not eligible")

# Bonus Challenges

# Check whether a number is even or odd.
number = int(input("Enter your number:"))
if number%2 == 0:
    print("Even")
else:
    print("Odd")

# Find the largest of three numbers.

num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
num3 = int(input("Enter third number"))
if num1>num2 and num1>num3:
    print(f"{num1} is largest number")
elif num2>num1 and num2>num3:
    print(f"{num2} is largest number")
else:
    print(f"{num3} is largest number")

# Check whether a year is a leap year.

year = int(input("Enter the year:"))
if year%400==0:
    print("This is leap year")
elif year%4==0:
    if year%100==0:
        print("This is not leap year")
    else:
        print("This is leap year")
else:
    print("This is not leap year")

# Build a simple calculator (+, -, *, /) using if-elif-else.

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
opr = input("Enter operator:")
if opr == '+':
    print(num1+num2)
elif opr == '-':
    print(num1-num2)
elif opr == '*':
    print(num1*num2)
else:
    print(num1/num2)

# Print whether a person is a child, teenager, adult, or senior based on age.

Age = int(input("Enter your age:"))
if Age < 13:
    print("Child")
elif Age >= 13 and Age < 19:
    print("Teenager")
elif Age >=19 and Age < 40:
    print("Adult")
else:
    print("Senior")