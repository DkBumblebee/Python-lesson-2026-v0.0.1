def main():
    # Build a pyramid of # symbols
    height = get_height("How tall(1-8)? ")
    
    for i in range(height + 1):
        for j in range(height-i):
             print(" ", end="")
        for j in range(i):
            print("*", end=" ")
        print()

def get_height(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num >= 1 and num <= 8:
                return num
            else:
                continue
        except ValueError:
            print("Invaild value")

main()