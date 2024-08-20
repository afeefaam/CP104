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

def day_name(day_num):
    """
    -------------------------------------------------------
    Returns the name of a day of the week given an integer day number.
    Day 1 is "Sunday", day 7 is "Saturday".
    Returns "Error" if the number is not valid.
    Use: day = day_name(day_num)
    -------------------------------------------------------
    Parameters:
        day_num - day number (1 <= int <= 7)
    Returns:
        day - name of a day of the week (str)
    ------------------------------------------------------
    """
    if day_num==1:
        day="Sunday"
    elif day_num==2:
        day="Monday"
    elif day_num==3:
        day="Tuesday"
    elif day_num==4:
        day="Wednesday"
    elif day_num==5:
        day="Thursday"
    elif day_num==6:
        day="Friday"
    elif day_num==7:
        day="Saturday"  
    else:
        day="Error"  
    return day

def pollution_ranking(air_quality_index):
    """
    -------------------------------------------------------
    Returns the pollution level given an AQI (Air Quality Index):
        "Good" - 0 to 50 AQI
        "Moderate" - 51 - 100 AQI
        "Unhealthy" for Sensitive Groups - 101 - 150 AQI
        "Unhealthy" - 151 - 200 AQI
        "Very Unhealthy" - 201 - 300 AQI
        "Hazardous" - 300+ AQI
    Returns "Error" if air_quality_index is negative.
    Use: pollution = pollution_ranking(air_quality_index)
    -------------------------------------------------------
    Parameters:
        air_quality_index - Air Quality Index (int)
    Returns:
        pollution - name of pollution level (str)
    ------------------------------------------------------
    """
    
    if 50>air_quality_index>0:
        pollution="Good"
    elif 100>air_quality_index>51:
        pollution="Moderate"
    elif 150>air_quality_index>101:
        pollution="Unhealthy"
    elif 200>air_quality_index>151:
        pollution="Unhealthy"
    elif 300>air_quality_index>201:
        pollution="Very Unhealthy"
    elif air_quality_index>=300:
        pollution="Hazardous"
    else:
        pollution="Error"
    return pollution

def largest_average(val1, val2, val3):
    """
    -------------------------------------------------------
    Returns the average of the two largest values of
    val1, val2, and val3.
    Use: average = largest_average(val1, val2, val3)
    -------------------------------------------------------
    Parameters:
        val1 - a number (float)
        val2 - a number (float)
        val3 - a number (float)
    Returns:
        average - the average of the two largest values of
            val1, val2, and val3 (float)
    ------------------------------------------------------
    """
    if val1>val3 and val2>val3:
        average=float((val1+val2)/2)
    elif val2>val1 and val3>val1:
        average=float((val2+val3)/2)
    elif val3>val2 and val1>val2:
        average=float((val3+val1)/2)
    else:
        average="None"
    return average

def colour_combine(rgb_colour1, rgb_colour2):
    """
    -------------------------------------------------------
    Determines the secondary rgb_colour from mixing two primary
    RGB (Red, Green, Blue) colours. The order of the colours
    is *not* significant.
    Returns "Error" if any of the rgb_colour parameter(s) are invalid.
        "red" + "blue": "fuchsia"
        "red" + "green": "yellow"
        "green" + "blue": "aqua"
        "red" + "red": "red"
        "blue" + "blue": "blue"
        "green" + "green": "green"
    Use: rgb_colour = colour_combine(rgb_colour1, rgb_colour2)
    -------------------------------------------------------
    Parameters:
        rgb_colour1 - a primary RGB rgb_colour (str)
        rgb_colour2 - a primary RGB rgb_colour (str)
    Returns:
        rgb_colour - a secondary RGB rgb_colour (str)
    -------------------------------------------------------
    """    
    if rgb_colour1=="red" and rgb_colour2=="blue" or rgb_colour1=="blue" and rgb_colour2 =="red":
        rgb_colour="fuchsia"
    elif rgb_colour1=="red" and rgb_colour2=="green" or rgb_colour1=="green" and rgb_colour2 =="red":
        rgb_colour="yellow"
    elif rgb_colour1=="green" and rgb_colour2=="blue" or rgb_colour1=="blue" and rgb_colour2 =="green":
        rgb_colour="aqua"
    elif rgb_colour1=="red" and rgb_colour2=="red":
        rgb_colour="red"
    elif rgb_colour1=="blue" and rgb_colour2=="blue":
        rgb_colour="blue"
    elif rgb_colour1=="green" and rgb_colour2=="green":
        rgb_colour="green"
    else:
        rgb_colour="Error"
    return rgb_colour

def hoo_rah(number):
    """
    -------------------------------------------------------
    hoo_rah takes an integer parameter and returns one of the following strings:
    "Hoo" if number is evenly divisible by 2
    "Rah" if number is evenly divisible by 7
    "Hoo Rah" if number is evenly divisible by both 2 and 7
    "Zip" if number is none of the above
    
    Use: message = hoo_rah(number)
    -------------------------------------------------------
    Parameters:
    number - a number (int)
    Returns:
    message - a message (str)
    -------------------------------------------------------
    """
    if number%2==0:
        message="Hoo"
    elif number%7==0:
        message="Rah"
    elif number%2==0 and number%7==0:
        message="Hoo Rah"
    else:
        message="Zip"
    return message
    