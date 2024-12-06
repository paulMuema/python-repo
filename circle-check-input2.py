from math import pi

while True:
    radius = float(input('Enter the radius: '))
    if radius < 0:
        print("radius must be a positive number")
    else:
        break

area = pi * radius * radius
print("The area of the circle is", area)
