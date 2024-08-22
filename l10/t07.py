"""
-------------------------------------------------------
[This program adds the max number to a file]
-------------------------------------------------------
Author:  Afeefa Malik
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2023-11-20"
-------------------------------------------------------
"""
# Imports
from functions import append_max_num
file_1="numbers.txt"
fh = open(file_1, "r+", encoding="utf-8")
num = append_max_num(fh)

print(f'File {file_1} is open for reading and w')
print(f'{num} is appended.')
fh.close()

