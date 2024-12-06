mark = int(input("Enter the numeric mark: "))
grade = 'invalid'
if mark <= 0 or mark > 100:
    print("Error: invalid mark")
elif mark >= 90:
    grade = 'A'
elif mark >= 80:
    grade  = 'B'
elif mark >= 70:
    grade = 'C'
elif mark >= 60:
    grade = 'D'
else:
    grade = 'F'

print("The grade is", grade)
