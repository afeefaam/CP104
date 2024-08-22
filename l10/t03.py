"""
-------------------------------------------------------
[This program determines the customer with the largest balance]
-------------------------------------------------------
Author:  Afeefa Malik
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2023-11-20"
-------------------------------------------------------
"""
# Imports
from functions import customer_best

file_1="customers.txt"
fh = open(file_1, "r", encoding="utf-8")
print(f'Find customer with largest balance: ')
print(customer_best(fh))
fh.close()
