"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Afeefa Malik
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2023-11-14"
-------------------------------------------------------
"""
# Imports
from functions import validate_code

product_code=input("Enter the product code: ")
category, digits, qualifiers = validate_code(product_code)

print(category, digits, qualifiers)
