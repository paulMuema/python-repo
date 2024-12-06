from math import pi

r = float(input("Radius: "))

if r > 0:
    print('The area of the circle is', pi * r * r)
else:
    print('ERROR! You entered an invalid radius')

print("Thank you")
