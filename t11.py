"""
-------------------------------------------------------
[This program determines the longest word]
-------------------------------------------------------
Author:  Afeefa Malik
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2023-11-20"
-------------------------------------------------------
"""
# Imports
from functions import find_longest

file_1="customers.txt"
fh = open(file_1, "r", encoding="utf-8")
word = find_longest(fh)
print(f'File {file_1} is open for reading.')
print(f'{word} is the last longest word.')
fh.close()

