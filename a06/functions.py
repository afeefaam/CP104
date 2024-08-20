"""
-------------------------------------------------------
[This program contains all of the functions]
-------------------------------------------------------
Author:  Afeefa Malik
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2023-11-08"
-------------------------------------------------------
"""

def total_wins():
    """
    -------------------------------------------------------
    Determines the total wins.
    Use: wins = total_wins()
    -------------------------------------------------------
    Returns:
        total_gold - total gold" appeared
        total_purple - total "purple"
    ------------------------------------------------------
    """
    total_purple=0
    total_gold=0
    game=input("Enter the game output (press enter to quit): ")
    while game!="":
        if game=="purple":
            total_purple+=1
        elif game=="gold":
            total_gold+=1
        game=(input("Enter the next game output (press enter to quit): "))

    return total_purple, total_gold
            
def detect_prime(number):
    """
    -------------------------------------------------------
    Determines if number is a prime number.
    Use: prime = detect_prime(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int > 1)
    Returns:
        prime - True if number is prime, False otherwise (bool)
    ------------------------------------------------------
    """
    #prime=False
    while number%number!=0:
        prime=False

    prime=True
            
    return prime
    
def interest_table(principal_amount, interest_rate, payment):
    """
    -------------------------------------------------------
    Prints a table of monthly interest and payments on a loan.
    Use: interest_table(principal_amount, interest_rate, payment)
    -------------------------------------------------------
    Parameters:
        principal_amount - original value of a loan (float > 0)
        interest_rate - yearly interest interest_rate as a % (float >= 0)
        payment - the monthly payment (float > 0)
    Returns:
        None
    --------------------------------------
    """
    print(f'Principal: {principal_amount:,.2f}')
    print(f'Interest Rate: {interest_rate:,.2f}')
    print(f'Monthly Payment: {payment:,.2f}')
    print()
    print("------------------------------------")
    print(f'Month  Interest   Payment   Balance')
    month=1
    while principal_amount>0:
        monthly=(interest_rate/12)/100*principal_amount
        if principal_amount-payment<0:
            payment=principal_amount+monthly
        pay_principal=payment-monthly
        if principal_amount-pay_principal<0:
            pay_principal=principal_amount
        principal_amount-=pay_principal
        print(f'{month:.0f} {monthly:10.2f} {payment:10.2f} {principal_amount:10.2f}')
        month+=1
    return None
    
def count_of_digits(number):
    """
    -------------------------------------------------------
    Counts the number of digits in an integer.
    Use: digits = count_of_digits(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int)
    Returns:
        digits - the number of digits in number (int)
    ------------------------------------------------------
    """
    count=0
    while number!=0:
        number=number//10
        count+=1
    return count
    
def factor_summation(number):
    """
    -------------------------------------------------------
    Determines the sum of factors of an integer not including
    the integer itself. An integer's factors are the whole numbers
    that the integer can be evenly divided by.
    Use: total = factor_summation(number)
    -------------------------------------------------------
    Parameters:
        number - a positive integer (int >= 1)
    Returns:
        total - the total of number's factors (int)
    --------------------------------
    """
    total=0
    integer=1
    while integer<number:
        if number%integer==0:
            total=integer+total
        integer+=1
    return total
