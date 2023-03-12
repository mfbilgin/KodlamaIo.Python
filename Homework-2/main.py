students = []

def take_student():
    name = input("Please enter the student name : ")
    surname = input("Please enter the student surname : ")
    if not name.isalpha() and not surname.isalpha():
        print("Please enter only letters.")
        return ""
    return (name.title() + " " + surname.title()).strip()

def add_student():
    print("\n---------------- Add Student ----------------\n")
    name_surname = take_student()
    if not name_surname == "":
        students.append(name_surname)
        print("Student added.")

def add_multiple_student():
    print("\n---------------- Add Multiple Student ----------------\n")
    count = int(input("Please enter the student count : "))
    for i in range(count):
        add_student()

def print_students():
    print("\n---------------- All Students ----------------\n")
    for student in students:
        print(student)

def print_school_number():
    print("\n---------------- Print School Number ----------------\n")
    name_surname = take_student()
    if name_surname not in students:
        print("Student not exists.")
        return
    print("student number : " + str(students.index(name_surname)))

def remove_student():
    print("\n---------------- Remove Student ----------------\n")

    name_surname = take_student()
    if name_surname not in students:
        print("Student not exists.")
        return
    students.remove(name_surname)
    print("student removed.")

def remove_multiple_student():
    print("\n---------------- Remove Multiple Student ----------------\n")
    print("enter 'Q' to quit")
    while True:
        name_surname = input("Please enter the student name and surname : ").title().strip()

        if name_surname == "Q" or name_surname == "q":
            break

        if  name_surname not in students:
            print("Student not exists.")
            continue

        students.remove(name_surname)
        print("student removed.")
        if len(students) == 0:
            print("All students removed.")
            break