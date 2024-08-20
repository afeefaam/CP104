"""
-------------------------------------------------------
[This file contains all of the functions]
-------------------------------------------------------
Author:  Afeefa Malik
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2023-11-04"
-------------------------------------------------------
"""
# Imports
def calc_factorial(number):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of number.
    Use: product = calc_factorial(number)
    -------------------------------------------------------
    Parameters:
        number - number to factorial (int > 0)
    Returns:
        product - number! (int)
    ------------------------------------------------------
    """
    product=1
    for i in range(number):
        i+=1
        product*=i
    return(product)

def calories_treadmill(per_min, minutes):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of number.
    Use: calories = calories_treadmill(per_min, minutes)
    -------------------------------------------------------
    Parameters:
        calories_burned - calories burned (float)
        minutes - number of minutes (int)
    Returns:
        None 
    ------------------------------------------------------
    """
    for i in range(5,minutes+1,5):
        calories=i*per_min
        print(f'{i}, {calories:.1f}')
    return None

def arrow_up(rows):
    """
    -------------------------------------------------------
    Outputs an arrow with hashtags.
    Use: arrow = arrow_up(rows)
    -------------------------------------------------------
    Parameters:
        rows - character (int)
    Returns:
        None 
    ------------------------------------------------------
    """
    print(" "*(rows-1)+"#")
    for i in range(1, rows):#rows 
        print(" " *(rows-i-1)+"#"+" "*(2*i-1)+"#")
    return None
def multiplication_table(start_num, stop_num):
    """
    -------------------------------------------------------
    Prints a multiplication table for values from start_num to stop_num.
    Use: multiplication_table(start_num, stop_num)
    -------------------------------------------------------
    Parameters:
        start_num - the range start value (int)
        stop_num - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """
    print("  ", end="")
    for i in range(start_num,stop_num+1):#rows
        print(f'{i:>3}', end="")
    print()
    print(" "*5+"-"*10)
    for i in range(start_num,stop_num+1):#columns
        print(f'{i:>3} |', end="")
        for j in range(start_num, stop_num+1):
            product=i*j
            print(f'{product:>3}', end="")
        print()
    return None

def range_addition(start, increment, count):
    """
    -------------------------------------------------------
    Uses a for loop to sum values from start by increment.
    Use: total = range_addition(start, increment, count)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        increment - the range increment (int)
        count - the number of values in the range (int)
    Returns:
        total - the sum of the range (int)
    ------------------------------------------------------
    """
    total=0
    for i in range(start, start+count*increment, increment):
        total+=i
    return total
