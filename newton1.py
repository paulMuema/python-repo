import math
x = float(input("Enter a number: "))
count = int(input("Enter the number of iterations: "))

guess = x/2

for i in range(count):
    guess = (guess + x / guess)/2

print(f"Guess: {guess :.5f}" )
print(f"Actual: {math.sqrt(x) :.5f}")

