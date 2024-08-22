"""
-------------------------------------------------------
[This program counts the frequency of characters]
-------------------------------------------------------
Author:  Afeefa Malik
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2023-12-01"
-------------------------------------------------------
"""
# Imports
from functions import count_frequency

matrix=[['a', 'b', 'c'], ['d', 'e', 'f'], ['a', 'b', 'c']]
char=str(input("Enter a character to find: "))


count = count_frequency(matrix, char)
print(count)