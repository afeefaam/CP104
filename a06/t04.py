"""
-------------------------------------------------------
[This program counts the number of digits in an integer.]
-------------------------------------------------------
Author:  Afeefa Malik
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2023-11-08"
-------------------------------------------------------
"""
# Imports

from functions import count_of_digits

number=int(input("Enter a number: "))

digits = count_of_digits(number)

print(f'There is {digits} digit(s).')
