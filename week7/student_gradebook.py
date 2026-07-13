# Grade Book Program

students = []

def add_student(name, grade):
    student = {"name": name, "grade": grade}
    students.append(student)

def show_results():
    for student in students:
        if student["grade"] >= 50:
            status= "Pass"
        else:
            status = "Fail"
        print(f"{student['name']}: {student['grade']}% — {status}")

# Add students using while loop
while True:
    name = input("Enter student name (or 'done' to stop): ")
    if name.lower() == "done":
        break
    grade = int(input("Enter students grade: "))
    add_student(name, grade)

print()
print("=" * 60)

show_results()