"""
-------------------------------------------------------
[Functions module]
-------------------------------------------------------
Author:  Afeefa Malik
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2023-10-13"
-------------------------------------------------------
"""
# Imports

import math
SQFT_PER_ACRE=43560
GRAVITATIONAL_ACCELERATION=9.8


def footage_to_acres(square_feet):
    """
    -------------------------------------------------------
    Converts square footage to acres.
    Use: acres = footage_to_acres(square_feet)
    -------------------------------------------------------
    Parameters:
        square_feet - area in square feet (float >= 0)
    Returns:
        acres - square_footage in acres (float)
    ------------------------------------------------------
    """
    
    acres=square_feet/SQFT_PER_ACRE
    return acres

def lawn_mow_time(width, length, speed):
    """
    -------------------------------------------------------
    Determines how long it takes to mow a rectangular lawn.
    Use: time = lawn_mow_time(width, length, speed)
    -------------------------------------------------------
    Parameters:
        width - width of a lawn in metres (float > 0)
        length - length of a lawn in metres (float > 0)
        speed - square metres cut per minute (float > 0)
    Returns:
        time_minutes - time required to mow the lawn (float)
    ------------------------------------------------------
    """
    time_minutes=(length*width)/speed
    return time_minutes

def extract_date(date_number):
    """
    -------------------------------------------------------
    Extracts the year, month, and day from a date number in the format YYYYMMDD.
    Use: year, month, day = extract_date(date_number)
    -------------------------------------------------------
    Parameters:
        date_number - a date number in the format YYYYMMDD (int)
    Returns:
        year - year portion of date_number (int)
        month - month portion of date_number (int)
        day - day portion of date_number (int)
    ------------------------------------------------------
    """
    year=date_number//10000
    month=date_number//100
    month2=month%year 
    day= date_number % month
    return year, month2, day

def multiply_fractions(num1, den1, num2, den2):
    """
    -------------------------------------------------------
    Calculates and returns fraction values.
    Use: num, den, product = multiply_fractions(num1, den1, num2, den2)
    -------------------------------------------------------
    Parameters:
        num1 - numerator of first fraction (int)
        den1 - denominator of first fraction (int != 0)
        num2 - numerator of second fraction (int)
        den2 - denominator of second fraction (int != 0)
    Returns:
        num - numerator of product (int)
        den - denominator of product (int)
        product - num / den (float)
    -------------------------------------------------------
    """
    num=int(num1*num2)
    den=int(den1*den2)
    product=float(num/den)
    return num, den, product

def falling_distance(time):
    """
    -------------------------------------------------------
    Calculates distance an object has fallen due to gravity given
    the time it is fallen.
    Use: distance = falling_distance(falling_time)
    -------------------------------------------------------
    Parameters:
        falling_time - time object has fallen in seconds (int >= 0)
    Returns:
        distance - distance object has fallen in metres (float)
    -------------------------------------------------------
    """
    distance=((time**2)*GRAVITATIONAL_ACCELERATION/2)
    return distance