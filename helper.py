# Jerry Luo
# 261238520

ERROR_DATE = ValueError("Input format incorrect!")
ERROR_QR = ValueError("File should contain only 0s and 1s!")

def convert_date(date_str):
    '''
    (str) -> dict
    Converts a date string in the format "dd/mm/yyyy" to a dictionary with keys "Day", "Month", and "Year".
    Raises a ValueError if the input format is incorrect.
    
    >>> convert_date("01/01/2005")
    {'Day': '01', 'Month': '01', 'Year': '2005'}
    >>> convert_date("00/00")
    Traceback (most recent call last): 
    ValueError: Input format incorrect!
    >>> convert_date("1/01/2005")
    Traceback (most recent call last): 
    ValueError: Input format incorrect!
    '''
    date_sep = date_str.split("/")
    date_dict = {"Day": 0, "Month": 0, "Year": 0}

    if len(date_sep) == 3:
        if len(date_sep[0]) == 2 and len(date_sep[1]) == 2 and len(date_sep[2]) == 4:
            date_dict["Day"] = date_sep[0]
            date_dict["Month"] = date_sep[1]
            date_dict["Year"] = date_sep[2]
            return date_dict
        else:
            raise ERROR_DATE
    else:
        raise ERROR_DATE

def get_data(file_path):
    '''
    (str) -> list of list of int
    Reads a file containing binary data (0s and 1s) and returns a nested list of integers.
    Raises a ValueError if the file contains any characters other than 0 or 1.
    
    >>> get_data("small_data.txt")
    [[0, 1], [1, 0]]
    >>> get_data("small_data_error.txt")
    Traceback (most recent call last):
    ValueError: File should contain only 0s and 1s!
    '''
    fileobj = open(file_path, "r")
    list1 = []

    for line in fileobj:
        new_line = line.strip()
        sublist = []

        for num in new_line:
            if num not in {'0', '1'}:
                raise ERROR_QR
            else:
                sublist.append(int(num))

        list1.append(sublist)

    fileobj.close()
    return list1