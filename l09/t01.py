"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Afeefa
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2023-11-14"
-------------------------------------------------------
"""
# Imports
from functions import is_hydroxide

chemical=str(input("Enter a chemical compound: "))

hydroxide = is_hydroxide(chemical)

print(hydroxide)
