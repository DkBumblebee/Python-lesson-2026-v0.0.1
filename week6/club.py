age = int(input("Age: "))
has_id = input("Do you have ID? (yes/no): ")

if age >= 18 and has_id == "yes":
    print("You may enter")
elif age >= 18 and has_id != "yes":
    print("Yopu need your ID")
else:
    print("You are too young")