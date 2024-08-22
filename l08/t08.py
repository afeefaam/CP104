"""
-------------------------------------------------------
[This program determines the index of a value]
-------------------------------------------------------
Author:  Afeefa Malik
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2023-11-07"
-------------------------------------------------------
"""
# Imports


from functions import linear_search

values=(input("Enter the values: "))
value=(input("Enter a value to find: "))

index = linear_search(values, value)

print(index)
