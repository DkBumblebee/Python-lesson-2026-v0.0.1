numbers = [3, 7, 2, 9, 5, 1, 8]
num = int(input("Check number(0-10): "))

if num in numbers:
    print(f"{num} is in list")
    # Find the index of an item
    print(f"The number is found in index {numbers.index(num)}")
else:
    print(f"{num} not found")