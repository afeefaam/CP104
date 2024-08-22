"""
-------------------------------------------------------
[This program contains all of the functions]
-------------------------------------------------------
Author:  Afeefa Malik
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2023-11-14"
-------------------------------------------------------
"""
# Imports
def is_hydroxide(chemical):
    """
    -------------------------------------------------------
    Determines if a chemical formula is a hydroxide.
    Use: hydroxide = is_hydroxide(chemical)
    -------------------------------------------------------
    Parameters:
        chemical - a chemical formula (str)
    Returns:
        hydroxide - True if chemical is a hydroxide (ends in 'OH'),
            False otherwise (boolean)
    -------------------------------------------------------
    """
    hydroxide=False
    if chemical[-2:]=="OH":
        hydroxide= True
    else:
        hydroxide= False
    return hydroxide

def validate_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code and prints whether the various parts are valid.
    A product code has three parts:
        The first three letters describe the product category and must
        all be in upper case.
        The next four digits are the product ID.
        The remaining characters describe the product's qualifiers,
        such as colour, size, etc. and always begins with an uppercase letter.
    Use: category, digits, qualifiers = validate_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a product code (str)
    Returns:
        category - True if three upper-case characters, False otherwise
        digits - True if four digits, False otherwise
        qualifiers - True if starts with 1 upper-case letter, False otherwise
    -------------------------------------------------------
    """
    
    category=False
    digits=False
    qualifiers=False
    
    if product_code[:3].isupper() and len(product_code[:3])==3:
        category=True
    if product_code[3:7].isdigit() and len(product_code[3:7])==4:
        digits=True
    if product_code[7:8].isupper():
        qualifiers=True
    return category, digits, qualifiers

def vowel_count(s):
    """
    -------------------------------------------------------
    Counts the number of vowels in a string. Does not include 'y'.
    Use: count = vowel_count(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        count - the number of vowels in s (int)
    -------------------------------------------------------
    """
    vowels="aeiouAEIOU"
    count=0

    for char in s:
        if char in vowels:
            count+=1
    return count

def text_analyze(txt):
    """
    -------------------------------------------------------
    Analyzes txt and returns the number of uppercase letters,
    lowercase letters, digits, and number of whitespaces in txt.
    Use: uppr, lowr, dgts, whtspc = text_analyze(txt)
    -------------------------------------------------------
    Parameters:
        txt - the text to be analyzed (str)
    Returns:
        uppr - number of uppercase letters in txt (int >= 0)
        lowr - number of lowercase letters in txt (int >= 0)
        dgts - number of digits in txt (int >= 0)
        whtspc - number of white spaces in the text (spaces, tabs, linefeeds) (int >= 0)
    ------------------------------------------------------
    """
    uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase="abcdefghijklmnopqrstuvwxyz"
    number="1234567890"
    
    upper=0
    lowr=0
    dgts=0
    whtspc=0
    
    for char in txt:
        if char in uppercase:
            upper+=1
        elif char in lowercase:
            lowr+=1
        elif char in number:
            dgts+=1
        elif char.isspace():
            whtspc+=1
        
    return upper, lowr, dgts,whtspc
    
def comma_period_replace(string):
    """
    -------------------------------------------------------
    Replaces all the commas with a period in s.
    Use: out = comma_period_replace(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        out - string with all commas replaced by a period (str)
    ------------------------------------------------------
    """
    out=string.replace(",", ".")
    return out

