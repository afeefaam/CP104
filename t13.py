"""
-------------------------------------------------------
[This program copies elements from one file to another]
-------------------------------------------------------
Author:  Afeefa Malik
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2023-11-20"
-------------------------------------------------------
"""
# Imports
from functions import file_copy

file_1="words.txt"
fh_1 = open(file_1, "r+", encoding="utf-8")
file_2="new_words.txt"
fh_2=open(file_2,"r+", encoding="utf-8")

file_copy(fh_1, fh_2)

print(f"Copying 'words.txt' to new_words.txt")
fh_1.close()
fh_2.close()

