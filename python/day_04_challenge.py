students = []

def add_student():
    student_id = int(input("Enter Student ID: "))
    name = input("Enter Student Name: ")
    course = input("Enter Course Name: ")
    marks = int(input("Enter Marks Obtain: "))
    new_student = {'id': student_id, 'name': name, 'course': course, 'marks': marks}
    students.append(new_student)
    print("Student added successfully.")

def view_students():
    for student in students:
        print(f"ID: {student['id']}")
        print(f"Name: {student['name']}")
        print(f"Course: {student['course']}")
        print(f"Marks: {student['marks']}")
        print('-' * 20)

def search_student(student_id):
    for student in students:
        if student_id == student['id']:
            print("Student Found")
            print(f"\nID: {student['id']}")
            print(f"Name: {student['name']}")
            print(f"Course: {student['course']}")
            print(f"Marks: {student['marks']}")
            return
    else:
        print("Student not found.")

def delete_student(student_id):
    for student in students:
        if student['id'] == student_id:
            students.remove(student)
            print("Student deleted successfully.")
            return
    else:
        print("Student not found.")

def display_top_scorer():
    top_student = students[0]

    for student in students:
        if student["marks"] > top_student["marks"]:
            top_student = student

    print(f"Highest Scorer: {top_student['name']}")
    print(f"Marks: {top_student['marks']}")

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Display Top Scorer")
    print("6. Exit")

    choice = int(input("Enter your choice:"))

    if choice == 1:
        add_student()

    elif choice == 2:
        view_students()

    elif choice == 3:
        student_id = input("Enter Student ID: ")
        search_student(student_id)

    elif choice == 4:
        student_id = input("Enter Student ID: ")
        delete_student(student_id)

    elif choice == 5:
        if len(students) == 0:
            print("No Students available.")
        else:
            display_top_scorer()

    elif choice == 6:
        break

    else:
        print("Invalid choice! Please try again.")