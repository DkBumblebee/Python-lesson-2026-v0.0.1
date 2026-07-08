'''
Your program must ask the user for the following information: 
1. First Name 
2. Last Name 
3. Age 
4. Gender 
5. Date of Birth 
6. Email Address 
7. Phone Number 
8. City 
9. Province 
10. Country 
11. Favourite Colour 
12. Favourite Food 
13. Dream Career 
14. Favourite Programming Language (for now you can enter Python )
'''

print("Welcome to Imentor you Foundation, \nPlease fill in this form\n")


firstname = input("Enter First Name: ")
lastname = input("Enter Last Name: ")
age = int(input("Enter Age: "))
gender = input("Enter Gender: ")
date_of_birth = input("Enter Date of Birth: ")
email = input("Enter Email Address: ")
phone_number = input("Enter Phone Number: ")
city = input("Enter City: ")
province = input("Enter Province: ")
country = input("Enter Country: ")
favourite_colour = input("Enter Favourite Colour: ")
favourite_food = input("Enter Favourite Food: ")
dreamCareer = input("Enter Dream Career: ")
favourite_programming_languag = input("Enter Favourite Programming Language: ")
favourite_movie = input("Enter Favourite Move: ")
favourite_sport = input("Enter Favourite Sport: ")

print("="*55)
print("             Personal Information card")
print("="*55)
print()
print("Personal Details")
print("-"*55)
print(f"First Name              : {firstname}")
print(f"Last name               : {lastname}")
print(f"Age                     : {age}")
print(f"Gender                  : {gender}")
print(f"Date of Birth           : {date_of_birth}")
print("\nContack Information")
print("-"*55)
print(f"Email Address           : {email}")
print(f"Phone number            : {phone_number}")
print("\nLocation")
print("-"*55)
print(f"City                    : {city}")
print(f"Province                : {province}")
print(f"Country                 : {country}")
print("\nPersonal Intrests")
print("-"*55)
print(f"Favourite Colour        : {favourite_colour}")
print(f"Favourite food          : {favourite_food}")
print(f"Dream Career            : {dreamCareer}")
print(f"Favourite Language      : {favourite_programming_languag}")
print(f"Favourite Movie         : {favourite_movie}")
print(f"Favourite Sport         : {favourite_sport}")

print()
print("=" * 55)
print("""
Thank you for completing your Personal Information Card! 
Have a wonderful day and keep practising Python!
""")
print("=" * 55)


option = input("Do you want a summary detail of you card(y/n)").lower()
if option == "n":
    print("BYE")
    quit()
print(f"Hello {firstname} {lastname}!")
print(f"You are a {age}-year-old apiring {dreamCareer} form {city}, {province}, {country}.")
print(f"Its great to know hat your favourite food is {favourite_food} and that 
you're learning {favourite_programming_languag}. ")    
print(f"Keep practising every day—you are one step closer to becoming an 
amazing programmer! ")