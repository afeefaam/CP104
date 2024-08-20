"""
-------------------------------------------------------
[This program description ouputs file statistics]
-------------------------------------------------------
Author:  Afeefa Malik
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2023-11-27"
-------------------------------------------------------
"""
# Imports
from functions import file_statistics

file_handle=open("file.txt", 'r', encoding="utf-8")

ucount, lcount, dcount, wcount, rcount = file_statistics(file_handle)
print(ucount, lcount, dcount, wcount, rcount)

file_handle.close()
