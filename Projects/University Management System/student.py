from person import Person

class Student(Person):

    def __init__(self, sid, name, age, gender, branch, course, email, marks):
        super().__init__(name, age, gender)

        self.sid = sid
        self.branch = branch
        self.course = course
        self.email = email
        self.marks = marks

    def percentage(self):
        return sum(self.marks) / len(self.marks)

    def display(self):
        super().display()

        print("Student ID :", self.sid)
        print("Branch :", self.branch)
        print("Course :", self.course)
        print("Email :", self.email)
        print("Marks :", self.marks)
        print("Percentage :", self.percentage())