from person import Person

class Employee(Person):

    def __init__(self, eid, name, age, gender, dept, salary, email):
        super().__init__(name, age, gender)

        self.eid = eid
        self.dept = dept
        self.salary = salary
        self.email = email
        self.subjects = []

    def add_subject(self, subject):
        self.subjects.append(subject)

    def display(self):
        super().display()

        print("Employee ID :", self.eid)
        print("Department :", self.dept)
        print("Salary :", self.salary)
        print("Email :", self.email)
        print("Subjects :", self.subjects)