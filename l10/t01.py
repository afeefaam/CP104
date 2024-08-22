"""
-------------------------------------------------------
[This program determines if a customer is in the record]
-------------------------------------------------------
Author:  Afeefa Malik
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2023-11-20"
-------------------------------------------------------
"""
# Imports
from functions import customer_record

file_1="customers.txt"
fh = open(file_1, "r", encoding="utf-8")
n=int(input("Enter a record number: "))
result = customer_record(fh, n)

print(result)
fh.close()
