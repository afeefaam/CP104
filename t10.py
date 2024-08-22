"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Afeefa Malik
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2023-11-14"
-------------------------------------------------------
"""
# Imports
from functions import text_analyze

txt=str(input("Enter a string: "))

uppr, lowr, dgts, whtspc = text_analyze(txt)

print(uppr, lowr, dgts, whtspc)