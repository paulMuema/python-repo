mark = int(input("Enter the numeric mark: "))
grade = 'invalid'
if mark <= 0:
    print("Error: mark must >= 0")
elif mark > 100:
    print("Error: mark must not exceed 100")
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
