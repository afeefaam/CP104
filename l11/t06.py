"""
-------------------------------------------------------
[This program determines the stats of a matrix]
-------------------------------------------------------
Author:  Afeefa Malik
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2023-12-01"
-------------------------------------------------------
"""
# Imports
from functions import matrix_stats

matrix=[[3, 4, -10, 10],[1,2,3,4]]

smallest, largest, total, average = matrix_stats(matrix)

print(smallest, largest, total, average)
