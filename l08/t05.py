"""
-------------------------------------------------------
[This program determines a list of lost numbers]
-------------------------------------------------------
Author:  Afeefa
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2023-11-07"
-------------------------------------------------------
"""
# Imports
from functions import get_lotto_numbers

n=int(input("Enter the amount of numbers in the list: "))
low=int(input("Enter the lowest number: "))
high=int(input("Enter the highest number: "))

numbers = get_lotto_numbers(n, low, high)
print(numbers)
