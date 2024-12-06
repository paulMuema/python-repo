from random import randint

secret = randint(1, 10)

for i in range(4):
    guess = int(input("Guess a number between 1 and 10: "))
    if not guess == secret:
        print("Wrong guess.")
    else:
        print("You got it. Congratulations!")
        break

print("The secret number is", secret)
