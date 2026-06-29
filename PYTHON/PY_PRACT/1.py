class Student:
    school_name = "abc school"
    @classmethod
    def change_school(cls,name):
        cls.school_name = name

s1 = Student()
s2 = Student()

print("Before change:")
print(s1.school_name)
print(s2.school_name)

Student.change_school("xyz school")
print("\nAfter change:")
print(s1.school_name)

Student.change_school("lmn school")
print("\nAfter change:")
print(s2.school_name)
