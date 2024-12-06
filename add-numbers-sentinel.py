"""
Allows any number of values to be entered
without the user specifying how many values
there are in advance.
The loop body may never execute.
"""
total = 0
number = int(input("Enter the first number or -1 to stop: "))
while number != -1:
    total = total + number
    number = int(input("Enter the next number or -1 to stop: "))

print("The sum of your numbers is", total)    
