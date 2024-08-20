"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Afeefa Malik
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2023-10-22"
-------------------------------------------------------
"""
# Imports
from functions import gic

value=int(input("Value: "))
years=int(input("Years: "))
rate=float(input("Rate: "))

final_value = gic(value, years, rate)
