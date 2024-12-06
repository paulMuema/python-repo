total = 0
numbers = int(input("How many numbers do you have? "))
for i in range(numbers):
    number = int(input("Enter a number: "))
    total = total + number

print("The sum of your numbers is", total)
