class Student:
    count = 0
    def __init__(self):
        Student.count+=1

    @staticmethod
    def show_count():
        print("Number of objects created:",Student.count)

s1 = Student()
s2 = Student()
s3 = Student()
s4 = Student()

Student.show_count()
