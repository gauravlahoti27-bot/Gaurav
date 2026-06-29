Students = {
    1 : {"name":"Aryan","grade":"A","attendance":92},
    2 : {"name":"Darsh","grade":"C","attendance":82},
    3 : {"name":"Viraj","grade":"B","attendance":89},
    4 : {"name":"Gaurav","grade":"A+","attendance":97},
}

print("Initial Student Records:")
for roll, details in Students.items():
    print(roll, ":", details)


Students[1] = {"name": "Kavya", "grade": "B", "attendance": 88}

print("\nAfter adding a new student:")
for Student in Students:
 print(Student,end="")
 print(Students[Student])

Students[2]["grade"] = "A"
Students[2]["attendance"] = 90

print("\nAfter updating Darsh's record:")
print(Students)

for details in Students.values():
    details["attendance"] += 1

print("\nAfter increasing attendance of all students by 1%:")
print(Students)

print("\nStudents with attendance below 90%:")
for roll, details in Students.items():
    if details["attendance"] < 90:
        print(details["name"], "-", details["attendance"], "%")

del Students[1]

print("\nAfter deleting student with Roll No 1:")
print(Students)
