from random import randint

random_number = randint(1, 100)
attempts = 10

print("Guess a number between 1 and 100")

while attempts > 0:
    user = input("Enter a number: ")

    if not user.isdecimal():
        print(f"Invalid Input! | {user}")
        continue
    elif int(user) < 1 or int(user) > 100:
        print("Out of Range!")
        continue

    user = int(user)

    print(f"You have {attempts} attempts to guess the number")
    attempts -= 1

    if user == random_number:
        print("Correct!")
        break
    elif user < random_number:
        print("Too low!")
    elif user > random_number:
        print("Too high!")
    else:
        print("Invalid Input!")

    print("_" * 30)

print("Game Over!")