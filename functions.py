"""
-------------------------------------------------------
[This program contains all of the functions]
-------------------------------------------------------
Author:  Afeefa Malik
ID:      169060299
Email:   mali0299@mylaurier.ca
__updated__ = "2023-11-27"
-------------------------------------------------------
"""
# Imports

def file_top(file_handle, count):
    """
    -------------------------------------------------------
    Prints first count lines of file_handle. Line numbering starts at 0.
    If length of file is shorter than count, stops printing after
    last line of file.
    Use: file_top(file_handle, count)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
        count - number of lines to print (int > 0)
    Returns:
        None
    -------------------------------------------------------
    """
    line=file_handle.readline()
    line_number=0
    while line!="" and line_number<count:
        print(line, end="")
        line=file_handle.readline()
        line_number+=1
    return 

def read_integers(file_handle):
    """
    -------------------------------------------------------
    Extracts positive integers from a file into a list of integers.
    Numbers are comma-delimited. Non-numeric tokens are ignored.
    Use: number_list = read_integers(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
    Returns:
        number_list - a list of integers from file_handle (list of int)
    -------------------------------------------------------
    """
    line=file_handle.readline()
    number_list=[]
    while line!="":
        values=line.strip().split(',')
        if len(values)>=4:
            for i in range(1,4):
                if values[i].isdigit():
                    number_list.append(int(values[i]))
        
        line=file_handle.readline()
    return number_list

def file_statistics(file_handle):
    """
    -------------------------------------------------------
    Evaluates the contents of a file by counting upper-case letters,
    lower-case letters, digits, white-spaces (including end-of-line
    characters), and remaining characters.
    Use: ucount, lcount, dcount, wcount, rcount = file_statistics(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
    Returns:
        ucount - The number of upper-case letters in the file (int)
        lcount - The number of lower-case letters in the file (int)
        dcount - The number of digits in the file (int)
        wcount - The number of white-space characters in the file (int)
        rcount - The number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    line=file_handle.readline()
    ucount=0
    lcount=0
    wcount=0
    dcount=0
    rcount=0
    while line!="":
        for char in line:
            if char.isupper():
                ucount+=1
            elif char.islower():
                lcount+=1
            elif char.isdigit():
                dcount+=1
            elif char.isspace():
                wcount+=1
            else:
                rcount+=1
        
        line=file_handle.readline()
    
    return ucount, lcount, dcount, wcount, rcount

def line_numbering(fh_read, fh_write):
    """
    -------------------------------------------------------
    Adds line numbers to a file. Contents of fh_write contain contents
    of fh_read where every line has line numbers added to the beginning
    of the line in the format [number]. Line numbering starts at 0.
    Put a single space after the line number.
    Use: line_numbering(fh_read, fh_write)
    -------------------------------------------------------
    Parameters:
        fh_read - file to read (file - open for reading)
        fh_write - file to write (file - open for writing)
    Returns:
        None
    -------------------------------------------------------
    """
    line_number=0
    for line in fh_read:
        fh_write.write(f'[{line_number}] {line}')
        line_number+=1
    return None
     
def student_stats(file_handle):
    """
    -------------------------------------------------------
    Get information from a file of file_handle and grades.
    Use: l_id, h_id, avg = student_stats(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - student information file in the format
            surname,forename,id,mark (file - open for reading)
    Returns:
        l_id - the id of the student with the lowest mark (str)
        h_id - the id of the student with the highest mark (str)
        avg - the average mark (float)
    -------------------------------------------------------
    """
    line=file_handle.readline().strip()
    low=100
    high=0
    avg=0
    count=0
    
    while line!="":
        data=line.strip().split(",")
        mark=float(data[3])
        id=int(data[2])
        count+=1

        if mark>high:
            high=mark
            h_id=str(id)
        if mark<low:
            low=mark
            l_id=str(id)
        avg+=mark
        line=file_handle.readline()

    avg=avg/count
    return l_id, h_id, avg
                