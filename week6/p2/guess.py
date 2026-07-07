import random

# Pick a random number
secret = random.randint(1, 100)
attempts = 0

# Loop 
while True:
    # Ask player for a guess
    guess = int(input("Guess (1-100): "))
    attempts += 1
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print(f"You got the number correct after {attempts}")
        break
