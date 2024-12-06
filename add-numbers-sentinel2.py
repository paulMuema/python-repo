"""
Allows any number of values to be entered
without the user specifying how many values
there are in advance.
Uses the empty string as a sentinel.
"""
total = 0
count = 0
data = input("Enter a score or nothing to quit: ")
while data != "":
    total = total + int(data)
    count = count + 1
    data = input("Enter the next score or nothing to quit: ")

if count == 0:
    print("The average score is 0")
else:
    print("The average score is", total/count)

