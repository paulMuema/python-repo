import math
x = float(input("Enter a number: "))

tolerance = 0.00001
guess = x/2

count = 0

while abs(guess ** 2 - x) > tolerance:
    guess = (guess + x / guess) / 2
    count = count + 1


print(f"Guess: {guess :.5f}" )
print(f"Actual: {math.sqrt(x) :.5f}")
print("It took", count, "iterations.")

