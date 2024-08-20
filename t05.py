"""
-------------------------------------------------------
[This program determines if the string is a word chain]
-------------------------------------------------------
Author:  Afeefa Malik
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2023-11-23"
-------------------------------------------------------
"""
# Imports
from functions import has_word_chain

words=eval(input("Enter a word chain (encloed in [] and a comma): "))
word_chain = has_word_chain(words)
print(word_chain)