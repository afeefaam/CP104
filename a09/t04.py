"""
-------------------------------------------------------
[This program makes line numbers on a new file]
-------------------------------------------------------
Author:  Afeefa Malik
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2023-11-27"
-------------------------------------------------------
"""
# Imports
from functions import line_numbering

fh_read=open("wilde.txt", 'r', encoding="utf-8")
fh_write=open("wilde_number.txt", 'w', encoding="utf-8")

print(line_numbering(fh_read, fh_write))

fh_read.close()
fh_write.close()
