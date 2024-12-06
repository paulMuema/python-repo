from math import pi

radius = float(input('Enter the radius: '))
if radius < 0:
    print("radius must be a positive number")
else:
    area = pi * radius * radius
    print("The area of the circle is", area)
