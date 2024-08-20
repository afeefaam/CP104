"""
-------------------------------------------------------
Calculates the amount earned grooming dogs
-------------------------------------------------------
Author:  Afeefa Malik
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2023-09-12"
-------------------------------------------------------
"""
#Constants
LARGE_DOG=75
SMALL_DOG=50

print("Number of large dogs groomed: ")
numoflargeDogs=int(input())
print("Number of small dogs groomed: ")
numofsmallDogs=int(input())
amountEarned=((LARGE_DOG*numoflargeDogs)+(SMALL_DOG*numofsmallDogs))
print("You earned ($): ", amountEarned)
