"""
-------------------------------------------------------
[This program contains all of the functions]
-------------------------------------------------------
Author:  Afeefa Malik
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2023-11-23"
-------------------------------------------------------
"""
# Imports
def add_spaces(sentence):
    """
    -------------------------------------------------------
    Create a new sentence with added space between words. Words start
    with upper-case characters.
    Use: spaced = add_spaces(sentence)
    -------------------------------------------------------
    Parameters:
        sentence - sentence that represents a sentence in which all the
            words are run together (no spaces), but the first character
            of each word is uppercase. sentence has at least one
            character (str)
    Returns:
        spaced - new sentence in which the words are separated
            by spaces and only the first word starts with
            an uppercase character (str)
    -------------------------------------------------------
    """
    spaced=sentence[0].upper()
    for i in sentence[1:]:
        if i.isupper():
            spaced+=" "+i.lower()
        else:
            spaced+=i
    return spaced    
    
def pluralize(string):
    """
    -------------------------------------------------------
    Pluralizes a string according to the rules:
        - if string ends with 's', 'sh', or 'ch', add 'es'
        - if string ends with 'y' but not 'ay' or 'oy', replace
            the 'y' with 'ies'
        - otherwise add 's'
    Use: pluralized = pluralize(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        pluralized - a pluralized_string version of string (str)
    -------------------------------------------------------
    """ 
    if string[-1:]=="s":
        pluralized=string.replace("s", "es")
    elif string[-2:]=="sh":
        pluralized=string.replace("sh", "es")
    elif string[-2:]=="ch":
        pluralized=string.replace("ch", "es")
    elif string[-1:]=="y" and string[-2:]!="ay" and string[-2:]!="oy":
        pluralized=string.replace("y", "ies")
    else:
        pluralized=string+"s"
    return pluralized
           
def common_end(str1, str2):
    """
    -------------------------------------------------------
    Returns the longest common ending of two strings.
    Use: suffix = common_end(str1, str2)
    -------------------------------------------------------
    Parameters:
        str1 - first string for ending comparison (str)
        str2 - second string for ending comparison (str)
    Returns:
        suffix - the longest common ending of str1 and str2 (str)
    -------------------------------------------------------
    """
    #if ending of first and ending of second are equal --> return the common endings
    #loop it --> 
    count=1
    suffix=""
    while str1[-count:]==str2[-count:]:
        count+=1
        suffix=str1[-count:]
    return suffix
    
def valid_isbn(isbn):
    """
    -------------------------------------------------------
    Determines if an ISBN string is valid. An ISBN string is valid if:
        - it consists of only digits and dashes ('-')
        - it contains 5 groups of digits separated by dashes
        - its first group of digits is either '978' or '979'
        - its final group of digits is a single digit
        - its entire length is 17 characters
    Use: is_valid = valid_isbn(isbn)
    -------------------------------------------------------
    Parameters:
        isbn - a string (str)
    Returns:
        is_valid - True if isbn is valid, False otherwise (boolean)
    -------------------------------------------------------
    """
    is_valid=True
    
    if len(isbn)!=17 or not isbn.replace('-','').isdigit():
        is_valid= False
    groups=isbn.split("-")
    if len(groups)!=5:
        is_valid= False
    if groups[0]not in {'978','979'}:
        is_valid= False
    if not groups[-1].isdigit() or len(groups[-1])!=1:
        is_valid= False
    for group in groups[1:-1]:
        if not group.isdigit():
            is_valid= False
    return is_valid
    
def has_word_chain(words):
    """
    -------------------------------------------------------
    Determines if a list of strings is a word chain. A word chain
    is a list of words in which the last character of a word in
    the list is the same as the first character of the next word
    in the list.
    Use: word_chain = has_word_chain(words)
    -------------------------------------------------------
    Parameters:
        words - a of strings (list of str, len > 1)
    Returns:
        word_chain - True if words is a word chain,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    word_chain=True
    count=1
    while count<len(words)-1:
        if words[count][-1]!=words[count+1][0]:
            word_chain=False
        count+=1
    return word_chain
        