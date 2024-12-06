# -*- coding: utf-8 -*-
"""
Created on Tue May 24 09:02:43 2022

@author: ambogho
"""
import math

sidea = float(input("Enter the length of one side: "))
sideb = float(input("Enter the lenght of the othe side: "))
sidea_sq = sidea * sidea
sideb_sq = sideb * sideb
hypotenuse = math.sqrt(sidea_sq + sideb_sq)

print("The lenght of the hypotenuse is", hypotenuse)
