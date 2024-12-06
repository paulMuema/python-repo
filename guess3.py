from random import randint

answer = input("Do you want to play? Y/N: ")
while answer == 'Y':
    secret = randint(1, 100)
    guess = int(input("Guess a number between 1 and 100: "))

    while guess != secret:
        if guess > secret:
            print("Too high")
        else:
            print("Too low")
        guess = int(input("Guess a number between 1 and 100: "))


    print("The secret number is", secret)
    answer = input("Do you want to play agian Y/N?")
print("Good bye!")
