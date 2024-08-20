"""
-------------------------------------------------------
Converts fahrenheight degrees to Celuis 
-------------------------------------------------------
Author:  Afeefa Malik
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2023-09-12"
-------------------------------------------------------
"""

#Constants
FREEZING_POINT=32

print("Enter a fahrenheit value: ")
fahrenheit = int(input())
celsius=int(fahrenheit-FREEZING_POINT)*5/9
print("Tempurature (C): ", int(celsius))
