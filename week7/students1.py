# Create a dictionary
student = {
    "name": "Thabo",
    "age": 22,
    "grade": 85,
    "passed": True
}

"""print(f"My name is {student["name"]}")
print(student["age"])
print(student["passed"])
print(student.get("grade")) # Safe mode
print("\n\n")
"""
# Add a new key
student["email"] = "thabosiba@gamil.com"

# Update a value
student["grade"] = 90
student["Favourite fruits"]= ["Apples", "Bananas", "Orange"]

name = "Thabo"
if "name" in student:
    print("Present")

# Loop through key
for key in student:
    print(f"{key.capitalize()}: {student[key]}")

print()

# Loop through values
for value in student.values():
    print(value)


print()
# Loop through both — most useful!
for key, value in student.items():
    print(f"{key}: {value}")


