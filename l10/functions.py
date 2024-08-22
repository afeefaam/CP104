"""
-------------------------------------------------------
[This program contains all of the functions]
-------------------------------------------------------
Author:  Afeefa Malik
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2023-11-20"
-------------------------------------------------------
"""
# Imports
def customer_record(fh, n):
    """
    -------------------------------------------------------
    Find the n-th record in a comma-delimited sequential file.
    Records are numbered starting with 0.
    Use: result = customer_record(fh, n)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        n - the number of the record to return (int > 0)
    Returns:
        result - a list of the fields of the n-th record if it exists,
            an empty list otherwise (list)
    -------------------------------------------------------
    """
    data=[]

    line_number=0
    line=fh.readline()
    while line!="" and line_number<n:
        line=fh.readline()
        line_number+=1
    if line_number==n and line!="":
        data = line.strip().split(",")

    fh.close()
    return data
    
def customer_best(fh):
    """
    -------------------------------------------------------
    Find the customer with the largest balance.
    Assumes file is not empty.
    Use: result = customer_best(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        result - the record with the greatest balance (list)
    -------------------------------------------------------
    """
    line=fh.readline()
    best=0.0
    result=[]
    while line!="":       
        values=line.strip().split(',')
        balance=float(values[3])
        if balance>best:
            best=balance
            result=values
        line=fh.readline()    
    return result

def append_max_num(fh):
    """
    -------------------------------------------------------
    Appends a number to the end of fh. The number appended
    is the maximum of all the numbers currently in the file.
    Assumes file is not empty.
    Use: num = append_max_num(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading/writing)
    Returns:
        num - the number appended to the file (int)
    ------------------------------------------------------
    """
    line=fh.readline()
    num=0.0
    while line!="":
        current_num=int(line)
        if current_num>num:
            num=current_num  
        line=fh.readline()
        
    fh.write(str(num)+"\n")  
    return num                   

def find_longest(fh):
    """
    -------------------------------------------------------
    Finds the last word with longest length in fh.
    Assumes file is not empty.
    Use: word = find_longest(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        word - the last word with the longest length in fh (str)
    ------------------------------------------------------
    """
    line=fh.readline()
    word=""
    while line!="":
        current_word=line.strip()
        if len(current_word)>=len(word):
            word=current_word
        line=fh.readline()
    return word

def file_copy(fh_1, fh_2):
    """
    -------------------------------------------------------
    Copies the contents of fh_1 to fh_2.
    Any contents of fh_2 are overwritten.
    Use: file_copy(fh_1, fh_2)
    -------------------------------------------------------
    Parameters:
        fh_1 - source file (file handle - already open for reading)
        fh_2 - target file (file handle - already open for writing)
    Returns:
        None
    ------------------------------------------------------
    """
    line=fh_1.readline()
    while line!="":
        fh_2.write(f'{line}')
        line=fh_1.readline()
    return None
    
    
