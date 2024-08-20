"""
-------------------------------------------------------
[This program outputs student stats]
-------------------------------------------------------
Author:  Afeefa Malik
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2023-11-27"
-------------------------------------------------------
"""
# Imports
from functions import student_stats

file_handle = open("students.txt", "r", encoding="utf-8")

l_id, h_id, avg = student_stats(file_handle)
print(l_id, h_id, avg)

file_handle.close()
