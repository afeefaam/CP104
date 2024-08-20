"""
-------------------------------------------------------
[This program prints a table of monthly interest and payments on a loan.]
-------------------------------------------------------
Author:  Afeefa Malik
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2023-11-08"
-------------------------------------------------------
"""
# Imports
from functions import interest_table

principal_amount=int(input("Enter the principal amount: "))
interest_rate=float(input("Enter the interest rate: "))
payment=int(input("Enter the payment: "))

interest_table(principal_amount, interest_rate, payment)

