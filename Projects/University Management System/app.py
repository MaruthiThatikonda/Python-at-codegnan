from university import University
from student import Student
from employee import Employee

uni = University("ABC University")

while True:

    print("\n UNIVERSITY MANAGEMENT SYSTEM ")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Remove Student")
    print("4. Add Employee")
    print("5. Display Employees")
    print("6. Remove Employee")
    print("7. Add Course")
    print("8. Show Courses")
    print("9. Total Students")
    print("10. Total Employees")
    print("11. Exit")

    choice = int(input("\nEnter Choice : "))

    if choice == 1:

        sid = int(input("Student ID : "))
        name = input("Name : ")
        age = int(input("Age : "))
        gender = input("Gender : ")
        branch = input("Branch : ")
        course = input("Course : ")
        email = input("Email : ")

        marks = []

        print("Enter Marks of 5 Subjects")

        for i in range(5):
            mark = float(input(f"Subject {i+1} : "))
            marks.append(mark)

        student = Student(sid, name, age, gender, branch, course, email, marks)

        uni.add_student(student)

        print("Student Added Successfully.")

    elif choice == 2:

        uni.show_students()

    elif choice == 3:

        sid = int(input("Enter Student ID : "))
        uni.remove_student(sid)

    elif choice == 4:

        eid = int(input("Employee ID : "))
        name = input("Name : ")
        age = int(input("Age : "))
        gender = input("Gender : ")
        dept = input("Department : ")
        salary = float(input("Salary : "))
        email = input("Email : ")

        employee = Employee(eid, name, age, gender, dept, salary, email)

        n = int(input("How Many Subjects : "))

        for i in range(n):
            subject = input(f"Subject {i+1} : ")
            employee.add_subject(subject)

        uni.add_employee(employee)

        print("Employee Added Successfully.")

    elif choice == 5:

        uni.show_employees()

    elif choice == 6:

        eid = int(input("Enter Employee ID : "))
        uni.remove_employee(eid)

    elif choice == 7:

        course = input("Course Name : ")
        uni.add_course(course)

    elif choice == 8:

        uni.show_courses()

    elif choice == 9:

        uni.total_students()

    elif choice == 10:

        uni.total_employees()

    elif choice == 11:

        print("Thank You...")
        break

    else:

        print("Invalid Choice")