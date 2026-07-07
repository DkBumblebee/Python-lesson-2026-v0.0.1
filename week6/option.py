# CS50 Week 1 — match/case for menu
choice = input("Choose (1, 2, or 3): ")


match choice:
    case "1":
        print("You chose Option 1")
    case "2":
        print("You chose Option 2")
    case "3":
        print("You chose Option 3")
    case _:
        print("Invalid choice")
