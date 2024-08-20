"""
-------------------------------------------------------
Calculates the mortgage monthly payments.
-------------------------------------------------------
Author:  Afeefa Malik
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2023-09-12"
-------------------------------------------------------
"""

principal=float(input('Mortgage principal: '))
years=int(input('Number of years: '))
interest=int(input('Yearly interest rate: '))

num_months= years*12

monthly_payment=principal*((interest/100/12)*(1+(interest/100/12))**(num_months))/((1+(interest/100/12))**(num_months)-1)
print("The monthly payments are: $", monthly_payment)
