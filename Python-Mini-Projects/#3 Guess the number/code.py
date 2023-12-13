import random

count = 0
lower_number, higher_number = 1, 10
random_number = random.randint(lower_number, higher_number)

print(f"Please guess the number between {lower_number} and {higher_number}")

while count < 5:
    user_guessed_number = int(input("Guess the number: "))

    if user_guessed_number > random_number:
        print("The number is lower.")
    elif user_guessed_number < random_number:
        print("The number is higher.")
    else:
        print("Congrates! , You guessed the number correctly")
        break

    count += 1
print(f"The random number is {random_number}")

