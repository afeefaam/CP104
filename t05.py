"""
-------------------------------------------------------
[This program calculates the compound interest]
-------------------------------------------------------
Author:  Afeefa Malik
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2023-09-28"
-------------------------------------------------------
"""

principal = float(input("Principal: "))
rate = float(input("Interest (%): "))
time = int(input("Number of years: "))
num_years = int(input("Number of times interest compounded per year: "))

compound_interest = principal*(((1+ ((rate/100.0)/num_years))**(num_years*time)))

print(f'Balance: {compound_interest}')