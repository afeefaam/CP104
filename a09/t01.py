"""
-------------------------------------------------------
[This program outputs lines in a file]
-------------------------------------------------------
Author:  Afeefa Malik
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2023-11-27"
-------------------------------------------------------
"""
# Imports
from functions import file_top

file_handle=open("file.txt", 'r', encoding="utf-8")
count=int(input("Enter the amount of lines you want to retrieve: "))

file_top(file_handle, count)

file_handle.close()
