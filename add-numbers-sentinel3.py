"""
Allows any number of values to be entered
without the user specifying how many values
there are in advance.
Uses break.
The loob body executes at least once.
"""
total = 0
count = 0
while True:
    data = input("Enter a score or return to quit: ")
    if data == "":
        break
    total = total + int(data)
    count = count + 1

if count == 0:
    print("The average is 0")
else:
    print("The average is", total/count)
