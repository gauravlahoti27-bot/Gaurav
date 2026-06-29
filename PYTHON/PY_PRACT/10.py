class Student:
    college_name = "Mumbai University"   # class variable

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_college(cls, new_name):
        cls.college_name = new_name

    def display(self):
        print(f"Student: {self.name}, College: {Student.college_name}")

s1 = Student("Rahul")
s2 = Student("Priya")

s1.display()
s2.display()

# Change class variable using one instance
s1.change_college("IIT Bombay")
print("After changing college name using s1:")
s1.display()
s2.display()   # Change reflected in s2 as well
