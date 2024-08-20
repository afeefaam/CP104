"""
-------------------------------------------------------
[This program contains all of the functions]
-------------------------------------------------------
Author:  Afeefa Malik
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2023-11-16"
-------------------------------------------------------
"""
# Imports
def list_factors(number):
    """
    -------------------------------------------------------
    Takes an integer greater than 0 and returns a list of 
    the factors that make up that number.
    Not including the number itself.
    Use: list_number = list_factors(number)
    -------------------------------------------------------
    Parameters: 
        number - a number (int)
    Returns:
        out - A list of factors (list of int)
    ------------------------------------------------------
    """
    out=[]
    for i in range(1, number):
        if number%i==0:
            out.append(i)
    return out
    
def list_positives():
    """
    -------------------------------------------------------
    Gets a list of numbers from a user and returns the positive ones.
    Negative numbers are ignored. Enter 0 to stop entries.
    Use: number_list = list_positives()
    -------------------------------------------------------
    Returns:
        number_list - A list of positive integers (list of int)
    ------------------------------------------------------
    """
    number_list=[]
    number=int(input("Enter a number (0 to stop): "))
    while number!=0:
        if number>0:
            number_list.append(number)
        number=int(input("Enter another number (0 to stop): "))
    return number_list
        
def get_indexes(numbers, target_number):
    """
    -------------------------------------------------------
    Finds the indexes of target_number in numbers.
    Use: index_list = get_indexes(numbers, target_number)
    -------------------------------------------------------
    Parameters:
        numbers - list of values (list)
        target_number - value to look for in num_list (*)
    Returns:
        index_list - list of indexes of target_number (list of int)
    -------------------------------------------------------
    """
    index_list=[]
    for i in range (len(numbers)):
        if numbers[i]==target_number:
            index_list.append(i)
    return index_list

def list_subtract(minuend, subtrahend):
    """
    -------------------------------------------------------
    Alters the contents of minuend so that it does not contain
    any values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are removed from the first list.
    Use: list_subtract(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to not include in difference (list)
    Returns:
        None
    ------------------------------------------------------
    """

    for value in subtrahend:
        while value in minuend:
            minuend.remove(value)
    return None

def verify_sorted(numbers):
    """
    -------------------------------------------------------
    Determines whether a list is sorted.
    Use: in_order, index = verify_sorted(numbers)
    -------------------------------------------------------
    Parameters:
        numbers - a list of numbers (list)
    Returns:
        in_order - True if numbers is sorted, False otherwise (bool)
        index - index of first value not in order,
            -1 if in_order is True (int)
    ------------------------------------------------------
    """
    in_order=True
    index=-1
    first=False
    for i in range(len(numbers)-1):
        if numbers[i]>numbers[i+1]:
            if first is False:
                index=i+1
                in_order=False
                first=True
    return in_order, index
        
