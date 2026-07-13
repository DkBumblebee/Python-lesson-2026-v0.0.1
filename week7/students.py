# for loop through every item
students = ["Thabo", "Lerato", "Sipho", "Zanele"]

for student in students:
    print(student)

print("\n\n")

# Loop with index
for s in range(len(students)):
    print(f"{s + 1}) Name: {students[s]} ")