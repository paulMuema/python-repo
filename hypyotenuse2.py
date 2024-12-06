# -*- coding: utf-8 -*-
"""
Created on Tue May 24 09:02:43 2022

@author: ambogho
"""
import math

sidea = float(input("Enter the length of one side: "))
sideb = float(input("Enter the lenght of the othe side: "))

hypotenuse = math.sqrt(sidea * sidea + sideb * sideb)

print("The length of the hypotenuse is", hypotenuse)

print("The length of the hypotenuse of a triangle with sides", sidea, "and", sideb, "is", hypotenuse)
print("Thank you!", end=' ')
print("Good bye.")
