"""
-------------------------------------------------------
Calculates seconds in different time units
-------------------------------------------------------
Author:  Afeefa Malik
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2023-09-21"
-------------------------------------------------------
"""
#Constants
HOURS=24 
MINUTES=60

seconds=int(input("Seconds: "))
s_perminutes=(seconds//MINUTES)
s_perhours = s_perminutes//MINUTES
days = s_perhours//HOURS

rem_h = s_perhours - (days * HOURS)
rem_m = s_perminutes - (s_perhours * MINUTES)
rem_s = seconds - (s_perminutes * MINUTES)

print(f'Days: {days} |Hours: {rem_h} |Minutes: {rem_m} |Seconds: {rem_s}')
