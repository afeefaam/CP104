"""
-------------------------------------------------------
[This program calculates the sum]
-------------------------------------------------------
Author:  Afeefa Malik
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2023-11-04"
-------------------------------------------------------
"""
# Imports
from functions import range_addition

start=int(input("Start: "))
increment=int(input("Increment: "))
count=int(input("Count: "))

total = range_addition(start, increment, count)

print(total)