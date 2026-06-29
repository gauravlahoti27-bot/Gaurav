class Student:
    def __init__(self, roll_number, name, marks):
        self.roll_number = roll_number
        self.name = name
        self.marks = marks
    def display(self):
        print("Child Details: ")
        print("Roll no: ",self.roll_number)
        print("Name: ",self.name) 
        print("Marks:",self.marks)

std1 = Student()
std1.display()

std2 = Student()
std2.display()