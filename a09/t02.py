"""
-------------------------------------------------------
[This program reads integers from a file]
-------------------------------------------------------
Author:  Afeefa Malik
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2023-11-27"
-------------------------------------------------------
"""
# Imports
from functions import read_integers

file_handle=open("file.txt", 'r', encoding="utf-8")

number_list = read_integers(file_handle)

print(number_list)

file_handle.close()
