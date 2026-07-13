# Multiple students stored in a list of dicts
students = [
    {"name": "Thabo", "grade": 85},
    {"name": "Lerato", "grade": 45},
    {"name": "Sipho", "grade": 92}
]


students[1]["grade"] = 66
for student in students:
    if student["grade"] >= 50:
        print(f"{student["name"]} has passed the grade")
    else:
         print(f"{student["name"]} has failed the grade")


