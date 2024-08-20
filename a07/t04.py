"""
-------------------------------------------------------
[This program removes a number from a list]
-------------------------------------------------------
Author:  Afeefa Malik
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2023-11-16"
-------------------------------------------------------
"""
# Imports
from functions import list_subtract

minuend=eval(input("Enter the first list (enclosed in []): "))
subtrahend=(input("Enter the value to remove: "))

print(list_subtract(minuend, subtrahend))
