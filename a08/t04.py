"""
-------------------------------------------------------
[This program determines if an isbn is valid]
-------------------------------------------------------
Author:  Afeefa Malik
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2023-11-23"
-------------------------------------------------------
"""
# Imports
from functions import valid_isbn

isbn=input("Enter a valid ISBN('###-#-########--#'): ")
is_valid = valid_isbn(isbn)
print(is_valid)
