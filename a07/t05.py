"""
-------------------------------------------------------
[This program determines if a list is sorted]
-------------------------------------------------------
Author:  Afeefa Malik
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2023-11-16"
-------------------------------------------------------
"""
# Imports
from functions import verify_sorted

numbers=eval(input("Enter a list of numbers (enclosed with []): "))

in_order, index = verify_sorted(numbers)

print(in_order, index)
