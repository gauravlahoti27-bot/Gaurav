print("Gautrav Lahoti B1 2501069")
students = {
    1: {"name": "Aryan", "grade": "A",  "attendance": 92},
    2: {"name": "Darsh", "grade": "C",  "attendance": 82},
    3: {"name": "Viraj", "grade": "B",  "attendance": 89},
    4: {"name": "Gaurav","grade": "A+", "attendance": 97}
}
print("Initial Student Records:")
for roll, details in students.items():
    print(roll, ":", details)


while True:
    print("\nMENU")
    print("1. Add student")
    print("2. Update student record")
    print("3. Increase attendance of all by 1%")
    print("4. Delete student record")
    print("5. See students below 90% attendance")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    # 1. Add student
    if choice == 1:
        roll = int(input("Enter roll number: "))
        if roll in students:
            print("Roll number already exists.")
        else:
            name = input("Enter name: ")
            grade = input("Enter grade: ")
            attendance = int(input("Enter attendance percentage: "))
            students[roll] = {
                "name": name,
                "grade": grade,
                "attendance": attendance
            }
            print("Student added.")

            print("\nStudent Records:")
            for r, d in students.items():
                print(r, d)

    # 2. Update student record
    elif choice == 2:
        roll = int(input("Enter roll number to update: "))
        if roll not in students:
            print("Student not found.")
        else:
            students[roll]["name"] = input("Enter new name: ")
            students[roll]["grade"] = input("Enter new grade: ")
            students[roll]["attendance"] = int(input("Enter new attendance: "))
            print("Record updated.")

            print("\nStudent Records:")
            for r, d in students.items():
                print(r, d)

    # 3. Increase attendance of all by 1%
    elif choice == 3:
        for r in students:
            students[r]["attendance"] += 1
            if students[r]["attendance"] > 100:
                students[r]["attendance"] = 100
        print("Attendance increased by 1%.")

        print("\nStudent Records:")
        for r, d in students.items():
            print(r, d)

    # 4. Delete student record
    elif choice == 4:
        roll = int(input("Enter roll number to delete: "))
        if roll in students:
            del students[roll]
            print("Student deleted.")

            print("\nStudent Records:")
            for r, d in students.items():
                print(r, d)
        else:
            print("Student not found.")

    # 5. See students below 90% attendance
    elif choice == 5:
        print("\nStudents below 90% attendance:")
        found = False
        for r, d in students.items():
            if d["attendance"] < 90:
                print(r, d)
                found = True
        if not found:
            print("None")

    # Exit
    elif choice == 6:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")
