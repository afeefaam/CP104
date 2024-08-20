"""
-------------------------------------------------------
[This program determines the sum of factors of an integer]
-------------------------------------------------------
Author:  Afeefa Malik
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2023-11-08"
-------------------------------------------------------
"""
# Imports
from functions import factor_summation

number=int(input("Enter a number: "))

total = factor_summation(number)

print(f'The total is: {total}')
