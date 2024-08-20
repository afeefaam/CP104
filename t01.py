"""
-------------------------------------------------------
[This program adds spaces to a string in a sentence]
-------------------------------------------------------
Author:  Afeefa Malik
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2023-11-23"
-------------------------------------------------------
"""
# Imports
from functions import add_spaces
sentence=str(input("Enter a sentence (with every first letter with a capital): "))
spaced = add_spaces(sentence)
print(spaced)