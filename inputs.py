# -*- coding: utf-8 -*-
"""
Created on Thu May 19 09:11:41 2022

@author: ambogho
"""

day = input("Enter the day of the week: ")
date = int(input("Enter the date: "))
amount = float(input("Ebter the amount of money: "))
price = 500

print("Today is", day, "the", str(date) + "th of May.")

print("Your change is", amount - price)

print("Next week", day, "will be the", str(date + 7) + "th.")