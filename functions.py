"""
-------------------------------------------------------
[This is the functions module]
-------------------------------------------------------
Author:  Afeefa Malik
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2023-10-22"
-------------------------------------------------------
"""

def sum_odd(num):
    """
    -------------------------------------------------------
    Sums and returns the total of all odd numbers from 1 to num (inclusive).
    Use: total = sum_odd(num)
    -------------------------------------------------------
    Parameters:
        num - an integer (int > 0)
    Returns:
        total - sum of all odd numbers from 1 to num (int)
    ------------------------------------------------------
    """
    total=0
    
    for i in range(1, num+1, 2):
        total=i +total
    return total

def draw_triangle(height, char):
    """
    -------------------------------------------------------
    Prints a triangle of height characters using
    the char character.
    Use: draw_triangle(height, char)
    -------------------------------------------------------
    Parameters:
        height - number of characters high (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    -------------
    """
    for i in range(1,height+1):
        print(" "*(height-i)+char*(2*i-1))
    
    return None
    
def treadmill(burnt_per_minute, start, end, inc):
    """
    -------------------------------------------------------
    Calculates and prints calories burnt on a treadmill over
    a given time range.
    Use: treadmill(burnt_per_minute, start, end, inc)
    -------------------------------------------------------
    Parameters:
        burnt_per_minute - calories burnt per minute (float > 0)
        start - start time in minutes (int > 0)
        end - end time in minutes (int >= start)
        inc - increment in minutes (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    total_burn = 0 
    for i in range(start, end+1, inc):
        total_burn= i * burnt_per_minute
        print(f"Calries burned after {i} minutes: {total_burn:,.1f}")
    return None

def gic(value, years, rate):
    """
    -------------------------------------------------------
    Calculates and prints a table of how much a GIC (Guaranteed
    Income Certificate) is worth over a number of years, and
    returns its final value.
    Use: final_value = gic(value, years, rate)
    -------------------------------------------------------
    Parameters:
        value - GICs initial value (int > 0)
        years - number of years to maturity (int > 0)
        rate - percent increase value per year (float > 0)
    Returns:
        final_value - the final value of the GIC (float)
    ------------------------------------------------------
    """
    print("Year        Value")
    print("-----------------")
    print(f'{0:2} {value:>14,.2f}')
    
    for i in range (1,years+1,1):
        value*=(1+rate/100)
        print(f'{i:2} {value:>14,.2f}')

    return value 
            

def statistics(n):
    """
    -------------------------------------------------------
    Asks a user to enter n values, then calculates and returns
    the minimum, maximum, total, and average of those values.
    Use: minimum, maximum, total, average = statistics(n)
    -------------------------------------------------------
    Parameters:
        n - number of values to process (int > 0)
    Returns:
        minimum - smallest of n values (float)
        maximum - largest of n values (float)
        total - total of n values (float)
        average - average of n values (float)
    ------------------------------------------------------
    """
    
    if n<=0:
        n=1
        minimum=maximum=total=average=0.0
    else:
        minimum=maximum=total=average=float(input("Enter the first value: "))
    
    for i in range(2, n+1):
        final_value=float(input(f"Enter the next value {i}: "))
        total+=final_value
        if final_value<minimum:
            minimum=final_value
        elif final_value>maximum:
            maximum=final_value
    average=total/n
  
    return minimum, maximum, total, average

        
    
    