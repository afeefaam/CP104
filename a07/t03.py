"""
-------------------------------------------------------
[This program outputs the index of a target number]
-------------------------------------------------------
Author:  Afeefa Malik
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2023-11-16"
-------------------------------------------------------
"""
# Imports
from functions import get_indexes

numbers=eval(input("Enter a list of numbers (enclosed in []): "))
target_number=int(input("Enter a target number: "))

index_list = get_indexes(numbers, target_number)

print(index_list)
