"""
-------------------------------------------------------
[This is the functions module]
-------------------------------------------------------
Author:  Afeefa Malik
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2023-10-18"
-------------------------------------------------------
"""
# Constants
GRAV_ACCEL=9.8

def get_weight(mass):
    """
    -------------------------------------------------------
    Describes a mass in terms of its weight. If its weight is > 1000 N,
    it is "heavy", less than 10 N it is "light", and "average" otherwise.
    weight = mass (kg)  acceleration due to gravity (9.8/m/s^2)
    Use: weight, message = get_weight(mass)
    -------------------------------------------------------
    Parameters:
        mass - mass of an object in kg (float > 0)
    Returns:
        weight - weight of an object in Newtons (float)
        message - description of weight of object (str)
    -------------------------------------------------------
    """
    weight=mass*GRAV_ACCEL
    if weight<10:
        message="light"
    elif weight>1000:
        message="heavy"
    else:
        message="average"
        
    return weight, message

def is_leap(year):
    """
    -------------------------------------------------------
    Determines if a year is a leap year. Every year that is
    exactly divisible by four is a leap year, except for years
    that are exactly divisible by 100, but these centurial years
    are leap years if they are exactly divisible by 400. For
    example, the years 1700, 1800, and 1900 are not leap years,
    but the years 1600 and 2000 are.
    Use: result = is_leap(year)
    -------------------------------------------------------
    Parameters:
        year - a year (int > 0)
    Returns:
        result - True if year is a leap year,
            False otherwise (boolean)
    ------------------------------------------------------
    """

    if year%400==0:
        leap_year=True
    elif year%100==0:
        leap_year=False
    elif year%4==0:
        leap_year=True
    else:
        leap_year=False    
    return leap_year
        
def roman_numeral(n):
    """
    -------------------------------------------------------
    Convert 1-10 to Roman numerals.
    Use: numeral = roman_numeral(n)
    -------------------------------------------------------
    Parameters:
        n - number to convert to Roman numerals (int)
    Returns:
        numeral - Roman numeral version of n, None if n is not
          between 1 and 10 inclusive. (str)
    -------------------------------------------------------
    """
    
    if n==1:
        numeral="I"
    elif n==2:
        numeral="II"
    elif n==3:
        numeral="III"
    elif n==4:
        numeral="IV"
    elif n==5:
        numeral="V"
    elif n==6:
        numeral="VI"
    elif n==7:
        numeral="VII"
    elif n==8:
        numeral="VIII"
    elif n==9:
        numeral="IX"
    elif n==10:
        numeral="X"
    else:
        numeral="Out of bounds"
    return numeral

def quadrant(x, y):
    """
    -------------------------------------------------------
    Determines location on a plane of an x, y coordinate.
    Use: location = quadrant(x, y)
    -------------------------------------------------------
    Parameters:
        x - x coordinate on a Cartesian plane (float)
        y - y coordinate on a Cartesian plane (float)
    Returns:
        location - one of: 'Quadrant 1', 'Quadrant 2', 'Quadrant 3'
          'Quadrant 4', 'X-Axis', 'Y-Axis', 'Origin' (str)
    -------------------------------------------------------
    """
    if x==0 and y==0:
        location="Origin"
    elif x==0 and y!=0 :
        location="Y-Axis" 
    elif y==0 and x!=0:
        location="X-Axis"
    elif x>0 and y>0:
        location="Quadrant 1"
    elif x<0 and y>0:
        location="Quadrant 2"
    elif x<0 and y<0:
        location="Quadrant 3"
    elif x>0 and y<0:
        location="Quadrant 4"
    else:
        location="None"
    return location

def ticket():
    """
    -------------------------------------------------------
    School play ticket price calculation.
    Asks user for their age, and if necessary, if they are
    a student at the school. Prices:
        Infant (age < 3): $0
        Senior (age >= 65): $4.00
        Student (10 <= age < 18): $3.00
            Student of this school: $1.00
        Adult (18 <= age < 65): $5.00
        Kid (3 <= age < 10): $2.00
    Use: price = ticket()
    -------------------------------------------------------
    Returns:
        price - the price of one ticket (float)
    -------------------------------------------------------
    """
    INFANT=3
    INFANT_COST=0
    SENIOR=65
    SENIOR_COST=4.00
    STUDENT=18
    STUDENT_COST=3.00
    STUDENT_SCHOOL_COST=1.00
    ADULT=18
    ADULT_COST=5.00
    KID=10
    KID_COST=2.00
    
    age = float(input("Enter your age: "))
    
    if age<INFANT:
        price=INFANT_COST
        
    elif age>=SENIOR:
        price=SENIOR_COST
        
    elif KID<=age<STUDENT:
        price=STUDENT_COST
        student=input("Are you a student of the school? (Y/N): ")
        if student=="Y":
            price=STUDENT_SCHOOL_COST
        else:
            price=STUDENT_COST
            
    elif ADULT<=age<SENIOR:
        price=ADULT_COST
        
    elif INFANT<=age<KID:
        price=KID_COST
        
    else:
        price="NA"
    return price
        