"""
-------------------------------------------------------
[This program uses decimal formatting]
-------------------------------------------------------
Author:  Afeefa Malik
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2023-09-27"
-------------------------------------------------------
"""

dirt = float(input("Enter amount of dirt (m^3): "))
gravel = float(input("Enter amount of gravel (m^3): "))
sand = float(input("Enter amount of sand (m^3): "))

total = dirt+gravel+sand

print("Material    Cubic Meters")
print(f"Dirt       {dirt:9.1f}")
print(f"Gravel     {gravel:9.1f}")
print(f"Sand       {sand:9.1f}")
print(f"Total      {total:9.1f}")
