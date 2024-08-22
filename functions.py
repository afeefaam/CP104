"""
-------------------------------------------------------
[This program contains all of the functions]
-------------------------------------------------------
Author:  Afeefa Malik
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2023-12-01"
-------------------------------------------------------
"""
# Imports
import random

def generate_matrix_num(rows, cols, low, high, value_type):
    """
    -------------------------------------------------------
    Generates a 2D list of numbers of the given type, 'float' or 'int'.
    (To generate random float number use random.uniform and to
    generate random integer number use random.randint)
    Use: matrix = generate_matrix_num(rows, cols, low, high, value_type)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the list (int > 0)
        cols - number of columns (int > 0)
        low - low value of range (float)
        high - high value of range (float > low)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        matrix - a 2D list of random numbers (2D list of float/int)
    -------------------------------------------------------
    """
    matrix=[]
    
    for i in range(rows):
        row=[]
        for j in range(cols):
            if value_type=="int":
                num=random.randint(low, high)
            elif value_type=="float":
                num=random.uniform(low, high)
            row.append(num)
        matrix.append(row)
    
    return matrix

def print_matrix_num(matrix, value_type):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list in \a formatted table.
    Prints float values with 2 decimal points and prints row and
    column headings.
    Use: print_matrix_num(matrix, 'float')
    Use: print_matrix_num(matrix, 'int')
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of values (2D list)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        None.
    -------------------------------------------------------
    """
    print(f" ", end="  ")
   
    for i in range(len(matrix[0])):
        print(f'{i:>5d}', end="")
    print()
    for i in range(len(matrix)):
        print(f'{i}', end="")
        
        for j in range(len(matrix[i])):
            if value_type=="int":
                print(f'{matrix[i][j]:>5d}', end="")
            elif value_type=="float":
                print(f'{matrix[i][j]:>5.2f}', end="")
        print()
    return None
     
def matrix_stats(matrix):
    """
    -------------------------------------------------------
    Returns statistics on a 2D list.
        Use: smallest, largest, total, average = matrix_stats(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list of float/int)
    Returns:
        smallest - the smallest number in matrix (float/int)
        largest - the largest number in matrix (float/int)
        total - the total of the numbers in matrix (float/int)
        average - the average of numbers in matrix (float/int)
    -------------------------------------------------------
    """
    smallest=matrix[0][0]
    largest=matrix[0][0]
    total=0
    count=0
    for row in matrix:
        for num in row:
            if num<smallest:
                smallest=num
            if num>largest:
                largest=num
            total+=num
            count+=1
    average=total/count            
    return smallest, largest, total, average
   
def count_frequency(matrix, char):
    """
    -------------------------------------------------------
    Count the number of appearances of the given character char
    in matrix.
    Use: count = count_frequency(matrix, char)
    -------------------------------------------------------
    Parameters:
        matrix - the matrix to search in it (2D list of str)
        char - character to search for it (str, len = 1)
    Returns:
        count - the number of appearances of char in the matrix (int)
    -------------------------------------------------------
    """
    rows=len(matrix)
    cols=len(matrix[0])
    count=0
    col_index=0
    while col_index<cols:
        row_index=0
        while row_index<rows:
            if matrix[row_index][col_index]==char:
                count+=1
            row_index+=1
        col_index+=1
    return count

def matrix_transpose(matrix):
    """
    -------------------------------------------------------
    Transpose the contents of matrix. (Swap the rows and columns.)
    Use: transposed = matrix_transpose(matrix):
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list (2D list of *)
    Returns:
        transposed - the transposed matrix (2D list of *)
    ------------------------------------------------------
    """
    transposed=[]
    for j in range(len(matrix[0])):
        row=[]
        for i in range(len(matrix)):
            row.append(matrix[i][j])
        transposed.append(row)
    return transposed
        