"""
-------------------------------------------------------
[This is the functions module]
-------------------------------------------------------
Author:  Afeefa Malik
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2023-11-01"
-------------------------------------------------------
"""
#Imports
from random import randint
import math


def hi_lo_game(high):
    """
    -------------------------------------------------------
    Plays a random higher-lower guessing game.
    Use: count = hi_lo_game(high)
    -------------------------------------------------------
    Parameters:
        high - maximum random value (int > 1)
    Returns:
        count - the number of guesses the user made (int)
    -------------------------------------------------------
    """
    #Constants
    count=0
    number=randint(1,high)
    guess=0
    while guess!=number:
        if number>guess:
            print("Too low, try again.")
            guess=int(input("Guess: "))
        elif number<guess:
            print("Too high, try again.")
            guess=int(input("Guess: "))
        count=count+1
    if guess==number:
        print("Congratulations!")
    return count
            
          
def power_of_two(target):
    """
    -------------------------------------------------------
    Determines the nearest power of 2 greater than or equal to
    a given target.
    Use: power = power_of_two(target)
    -------------------------------------------------------
    Parameters:
        target - value to find nearest power of 2 (int >= 0)
    Returns:
        power - first power of 2 >= target (int)
    -------------------------------------------------------
    """
    #Constant
    power=1
    while power<target:
        power*=2
    return power

def positive_statistics():
    """
    -------------------------------------------------------
    Asks a user to enter a series of positive numbers, then calculates
    and returns the minimum, maximum, total, and average of those numbers.
    Stop processing values when the user enters a negative number.
    The first number entered must be positive.
    Use: minimum, maximum, total, average = positive_statistics()
    -------------------------------------------------------
    Returns:
        minimum - smallest of the entered values (float)
        maximum - largest of the entered values (float)
        total - total of the entered values (float)
        average - average of the entered values (float)
    ------------------------------------------------------
    """
    #Constants
    sum=0.0
    num=0.0
    max=float('-inf')
    min=float('inf')
    
    user=float(input("Enter the first value: "))

    while user>-1:
        sum=sum+user
        num=num+1
        
        if user>max:
            max=user
            print(f'The {max} is')
        if user<min:
            min=user
            print("The min is: ",min)
        user=float(input("Enter the next value: "))
        average=sum/num
    return min, max, sum, average
 

def meal_costs():
    """
    -------------------------------------------------------
    Asks a user the costs of breakfast, lunch, and supper for each
    day the user was away. Assumes there is at least one day, and
    after entering data for each day asks the user whether they want
    to enter data for another day. Calculates total_per_day costs for meals.
    Use: b_total, l_total, s_total, a_total = meal_costs()
    -------------------------------------------------------
    Returns:
        b_total - total_per_day breakfasts cost (float)
        l_total - total_per_day lunches cost (float)
        s_total - total_per_day suppers cost (float)
        a_total - all meals cost (float)
    ------------------------------------------------------
    """
    #Constants
    day=1
    another="Y"
    a_total=0
    b_total=0
    l_total=0
    s_total=0
    
    while another!="N":
        print(f'For day {day}')
        breakfast=float(input("How much was breakfast?: "))
        lunch=float(input("How much was lunch?: "))
        supper=float(input("How much was supper?: "))
        
        total=breakfast+lunch+supper
        a_total = a_total + total
        b_total = b_total + breakfast
        s_total = s_total + supper
        l_total = l_total +lunch
        
        
        another=str(input("Were you away another day? (Y/N)"))
        total=0
        breakfast=0
        lunch=0
        supper=0
        day+=1
        
    return b_total, l_total, s_total,a_total
    

def employee_payroll():
    """
    -------------------------------------------------------
    Calculates and returns the weekly employee payroll for all employees
    in an organization. For each employee, ask the user for the employee ID
    number, the hourly wage rate, and the number of hours worked during a week.
    An employee number of zero indicates the end of user input.
    Each employee is paid 1.5 times their regular hourly rate for all hours
    over 40. A TAX amount of 3.625 percent of gross salary is deducted.
    Use: total, average = employee_payroll()
    -------------------------------------------------------
    Returns:
        total - total net employee wages (i.e. after SALES_TAXes) (float)
        average - average employee net wages (float)
    ------------------------------------------------------
    """
    #Constants
    totalmoney=0
    total=0
    OVERTIME=40
    SALES_TAX=0.03625
    OVERTIME_RATE=1.5
    number_employees=0

    #Input
    id=int(input("Employee ID: "))
   
    while id!=0:
        wage=float(input("Hourly wage rate: "))
        hours_worked=int(input("Hours worked: "))
        
        if hours_worked<OVERTIME:
            totalmoney=hours_worked*wage
            tax=totalmoney*SALES_TAX
            totalmoney=totalmoney-tax
            
            print(f'Net payment for employee {id}: ${totalmoney:,.2f}')
            
            total=total+totalmoney
            number_employees=number_employees+1
        
        elif hours_worked>=OVERTIME:
            totalmoney=OVERTIME*wage
            new_hours_worked=hours_worked-OVERTIME
            new_wage=wage*OVERTIME_RATE
            new_total=new_wage*new_hours_worked
            totalmoney=totalmoney+new_total
            tax=totalmoney*SALES_TAX
            totalmoney=totalmoney-tax
            
            print(f'Net payment for employee {id}: ${totalmoney:,.2f}')
            
            total=total+totalmoney
            number_employees=number_employees+1
        
        average=total/number_employees
        id=int(input("Employee ID: "))
        
    return total, average
    
