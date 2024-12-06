# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 23:10:23 2022
temperature using while loop
@author: hp
"""

temp = float(input("Enter your temperature in Celsius: "))

while temp < 0:
    print("Input is invalid")
    temp = float(input("Enter your temperature in Celsius: "))
else: 
    fah = 9/5 * temp + 32
    print("Your temperature in Fahrenheit is ", fah)
    
    