"""
-------------------------------------------------------
[This program returns the common suffix of two strings]
-------------------------------------------------------
Author:  Afeefa Malik
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2023-11-23"
-------------------------------------------------------
"""
# Imports
from functions import common_end

str1=str(input("Enter the first word: "))
str2=str(input("Enter the second word: "))
suffix = common_end(str1, str2)
print(suffix)
