class University:

    def __init__(self, name):

        self.name = name
        self.students = {}
        self.employees = {}
        self.courses = []

    # Student Methods

    def add_student(self, student):
        self.students[student.sid] = student

    def remove_student(self, sid):

        if sid in self.students:
            del self.students[sid]
            print("Student Removed Successfully.")
        else:
            print("Student Not Found.")

    def show_students(self):

        if len(self.students) == 0:
            print("No Students Found.")
        else:
            for student in self.students.values():
                student.display()
                print("----------------------")

    # Employee Methods

    def add_employee(self, employee):
        self.employees[employee.eid] = employee

    def remove_employee(self, eid):

        if eid in self.employees:
            del self.employees[eid]
            print("Employee Removed Successfully.")
        else:
            print("Employee Not Found.")

    def show_employees(self):

        if len(self.employees) == 0:
            print("No Employees Found.")
        else:
            for employee in self.employees.values():
                employee.display()
                print("----------------------")

    # Course Methods

    def add_course(self, course):

        self.courses.append(course)
        print("Course Added Successfully.")

    def show_courses(self):

        if len(self.courses) == 0:
            print("No Courses Available.")
        else:
            print("Courses:")
            for course in self.courses:
                print(course)

    # Count

    def total_students(self):
        print("Total Students :", len(self.students))

    def total_employees(self):
        print("Total Employees :", len(self.employees))