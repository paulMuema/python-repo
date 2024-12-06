from random import randint

secret = randint(1, 10)

for i in range(3):
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == secret:
        print("congratulations! You got it.")

print("The secret number is", secret)
