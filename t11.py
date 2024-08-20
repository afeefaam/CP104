"""
-------------------------------------------------------
Calculates the annual profit of a company
-------------------------------------------------------
Author:  Afeefa Malik
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2023-09-12"
-------------------------------------------------------
"""
#Constants
PROFIT_PERCENTAGE=0.18

projected_annualSales=float(input("Enter the projected annual sales: "))
PROFIT=projected_annualSales*PROFIT_PERCENTAGE
print(f'The projected profit on sales of {projected_annualSales} is {PROFIT}')