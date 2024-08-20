"""
-------------------------------------------------------
[This program calculates calories burned]
-------------------------------------------------------
Author:  Afeefa Malik
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2023-11-04"
-------------------------------------------------------
"""
# Imports
from functions import calories_treadmill

per_min=float(input("Enter the calories burned: "))
minutes=int(input("Enter the minutes ran: "))
calories = calories_treadmill(per_min, minutes)

print(calories)
