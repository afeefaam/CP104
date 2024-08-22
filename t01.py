"""
-------------------------------------------------------
[This program determines a day of the week given a number]
-------------------------------------------------------
Author:  Afeefa Malik
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2023-11-07"
-------------------------------------------------------
"""
# Imports
from functions import get_weekday_name

d=int(input("Enter a number (1-7): ").strip())
name = get_weekday_name(d)

print(name)