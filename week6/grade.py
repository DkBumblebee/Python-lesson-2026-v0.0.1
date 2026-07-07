score = int(input("Enter score: "))

if score == 100:
    print("Perfect score!")
elif score >= 75:
    print("Distinction")
elif score >= 50:
    print("passed")
else:
    print("Fail")