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
from functions import treadmill 

burnt_per_minute = float(input("burnt per minute: "))
start = int(input("Start: "))
end = int(input("End: "))
inc = int(input("Increment: "))



treadmill(burnt_per_minute, start, end, inc)
