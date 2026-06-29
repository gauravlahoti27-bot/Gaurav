import random
num = random.randint(1,100)
while True:

    guess = int(input("Guess a number between 1 and 100: "))
    if guess == num:
        print("Congratulations! You guessed the number.")
        break
    elif guess < num:
        print("Too low! Try again.")
    elif guess > num:
        print("Too high! Try again.")
    elif guess < 1 or guess > 100:
        print("Invalid input. Please enter a number between 1 and 100.")
    else:
        print("Wrong guess. The number was", num)