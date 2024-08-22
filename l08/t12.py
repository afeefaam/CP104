"""
-------------------------------------------------------
[This program determines the sum of two lists]
-------------------------------------------------------
Author:  Afeefa Malik
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2023-11-07"
-------------------------------------------------------
"""
# Imports
from functions import list_sums

source1=(input("Enter the first list: "))
source2=(input("Enter the second list: "))

target = list_sums(source1, source2)

print(target)
