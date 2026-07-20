class Person:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        print("Name :", self.name)
        print("Age :", self.age)
        print("Gender :", self.gender)