# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 22:53:38 2022
Calculating temperature using If loop
@author: hp
"""

temp = float(input("Enter a temperature in Celsisus: "))
if temp < 0:
    print("Input is invalid, try again")
else:
    fah = 9/5 * temp + 32
    print("Your temp in fahrenheit is ",fah)