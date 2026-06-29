'''
A program that asks user whether they want to add, divide, subtract or multiply

'''

def main():
    print("Welcome")
    print('''Do you want to: 
    a. Add
    b. Subtract
    c. Multiply
    d. Divide
    e. Squar
    f. Combo
    q. Quit
     ''')

    choice = input("Input: ")
    if choice == "q":
        print("Goodbye")
        quit()


    x = int(input("Whats x: "))
    y= int(input("Whats y: "))

    if choice == "a":
        num = add(x, y)
    elif choice == "b":
        num = sub(x, y)
    elif choice == "c":
        num = mul(x, y)
    elif choice == "d":
        num =div(x, y)
    elif choice == "e":
       num= square(x)
    elif choice == "f":
        print(f"When adding num is {add(x, y)} and when subtracting num is {sub(x,y)}")
        print(f"When dividing num is {div(x, y)} and when mulitiplying num is {mul(x, y)}")
        print(F"The square of x is {squar(x)}")
        quit()
    else:
        print("Invalid number on the input field. ")
        quit()
    print(num)





def add(a, b):
    return a + b

def sub(a, b):
    return a - b 

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def square(a):
    return a ** 2


main()