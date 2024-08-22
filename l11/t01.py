"""
-------------------------------------------------------
[This program generates a matrix]
-------------------------------------------------------
Author:  Afeefa Malik
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2023-12-01"
-------------------------------------------------------
"""
# Imports
from functions import generate_matrix_num

rows=3
cols=4
low=-10
high= 10
type="float"

matrix = generate_matrix_num(rows, cols, low, high, type)
print(matrix)
