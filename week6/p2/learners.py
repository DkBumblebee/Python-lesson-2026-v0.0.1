# Create a dictionary
student = {
    "name": "Thabo",
    "age": 22,
    "grade": 85,
    "passed": True
}

# Access by key
print(student["name"])   # Thabo
print(student.get("grade")) # 85 (safer)