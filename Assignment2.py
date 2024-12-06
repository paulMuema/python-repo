# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 09:22:09 2022

@author: hp
"""
text = input("Input your text: ")
textNumber = len(text)

print("The number of characters of your string are",textNumber)
for i in range(0,10):
   print(i, text)

print("The first character of your text is",text[0])
print("The first three characters of your string are",text[:3])
print("The last three characters of the string are",text[-3:])
print ("Your text backwards is",text[::-1])
if len(text) <= 6:
    print("Seventh character cannot be found!")
else:
    print("The seventh character of your string is",text[6])
print("The text with the first and last characters removed are",text[1:-1])
print("Your text in all caps is", text.upper())
print("Your text will all As replaced with Es is", text.replace('a','e'))

