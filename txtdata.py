import helper
import copy

class TxtData:
    '''
    A class to represent a 2D data structure with rows and columns.
    '''
    def __init__(self, data):
        '''
        (list of list of int) -> None
        Initializes a TxtData object with a deep copy of the input data.
        The data attribute is a nested list of integers, and rows and cols represent the dimensions of the data.
        
        >>> my_list_simple = [[1, 2, 3], [4, 5, 6]]
        >>> my_txt_simple = TxtData(my_list_simple)
        >>> my_txt_simple.rows
        2
        >>> my_txt_simple.cols
        3
        '''
        copied_data = copy.deepcopy(data)
        self.data = copied_data
        self.rows = len(copied_data)
        self.cols = len(copied_data[0])
    
    def __str__(self):
        '''
        (None) -> str
        Returns a string representation of the TxtData object indicating the number of rows and columns.
        
        >>> my_txt_simple = TxtData([[1, 2, 3], [4, 5, 6]])
        >>> print(my_txt_simple)
        This TxtData object has 2 rows and 3 columns.
        '''
        return f"This TxtData object has {self.rows} rows and {self.cols} columns."
    
    def get_pixels(self):
        '''
        (None) -> int
        Returns the total number of pixels (rows × columns) in the data.
        
        >>> my_txt_simple = TxtData([[1, 2, 3], [4, 5, 6]])
        >>> my_txt_simple.get_pixels()
        6
        '''
        return self.rows * self.cols
    
    def get_data_at(self, row, col):
        '''
        (int, int) -> int
        Returns the value at the specified row and column in the data.
        Raises a ValueError if the row or column is out of bounds.
        
        >>> my_txt_simple = TxtData([[1, 2, 3], [4, 5, 6]])
        >>> my_txt_simple.get_data_at(0, 0)
        1
        >>> my_txt_simple.get_data_at(3, 0)
        Traceback (most recent call last):
        ValueError: Index out of bound!
        '''
        if row >= self.rows or col >= self.cols or row < 0 or col < 0:
            raise ValueError("Index out of bound!")
        return self.data[row][col]
        
    def pretty_save(self, file_name):
        '''
        (str) -> None
        Saves the data in a prettier format where "1"s are replaced with "■" and "0"s with "  ".
        The formatted data is saved to a file with the given name.
        
        >>> my_txt = TxtData([[1, 0], [0, 1]])
        >>> my_txt.pretty_save("pretty_output.txt")
        '''
        fileobj = open(file_name, "w", encoding="utf-8")
        for r in range(self.rows):
            for c in range(self.cols):
                if self.data[r][c] == 1:
                    fileobj.write("\u2588\u2588")
                else:
                    fileobj.write("  ")
            fileobj.write("\n")
        fileobj.close()

    def equals(self, another_data):
        '''
        (TxtData) -> bool
        Returns True if the data of this TxtData object is equal to the data of another TxtData object.
        
        >>> my_txt1 = TxtData([[1, 2], [3, 4]])
        >>> my_txt2 = TxtData([[1, 2], [3, 4]])
        >>> my_txt1.equals(my_txt2)
        True
        '''
        return self.data == another_data.data
    
    def approximately_equals(self, another_data, precision):
        '''
        (TxtData, float) -> bool
        Returns True if the data of this TxtData object is approximately equal to the data of another TxtData object.
        The precision parameter determines the maximum allowed inconsistency rate.
        
        >>> my_txt1 = TxtData([[1, 0], [0, 1]])
        >>> my_txt2 = TxtData([[1, 0], [1, 1]])
        >>> my_txt1.approximately_equals(my_txt2, 0.5)
        True
        '''
        count = 0
        total = self.rows * self.cols
        for row in range(self.rows):
            for col in range(self.cols):
                if self.data[row][col] != another_data.data[row][col]:
                    count += 1
        return (count / total) <= precision