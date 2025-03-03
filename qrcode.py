import helper
import txtdata as txt

class QRCode:
    '''
    A class to represent a QR code with data, owner, last update date, and error correction capability.
    '''
    def __init__(self, file_path, last_update_date="00/00/0000", owner="Default Owner", error_correction=0.0):
        '''
        (str, str, str, float) -> None
        Initializes a QRCode object with data from the specified file, last update date, owner, and error correction capability.
        
        >>> my_qrcode = QRCode("qrcode_binary.txt", "01/09/2024", "Vivian", 0.1)
        >>> my_qrcode.last_update_date['Day']
        '01'
        >>> my_qrcode.owner
        'Vivian'
        '''
        self.last_update_date = helper.convert_date(last_update_date)
        self.owner = owner
        self.error_correction = error_correction
        self.data = txt.TxtData(helper.get_data(file_path))

    def __str__(self):
        '''
        (None) -> str
        Returns a string representation of the QRCode object, including the owner, last update year, and data dimensions.
        
        >>> my_qrcode = QRCode("qrcode_binary.txt", "01/09/2024", "Vivian", 0.1)
        >>> print(my_qrcode)
        The QR code was created by Vivian and last updated in 2024.
        The details regarding the QR code file are as follows:
        This TxtData object has 33 rows and 33 columns.
        '''
        year = self.last_update_date["Year"]
        rows = self.data.rows
        cols = self.data.cols
        return f"The QR code was created by {self.owner} and last updated in {year}.\n" + \
               f"The details regarding the QR code file are as follows:\n" + \
               f"This TxtData object has {rows} rows and {cols} columns."
    
    def equals(self, another_qrcode):
        '''
        (QRCode) -> bool
        Returns True if this QRCode object is equal to another QRCode object in terms of data and error correction capability.
        
        >>> my_qrcode = QRCode("qrcode_binary.txt", "01/09/2024", "Vivian", 0.1)
        >>> my_qrcode_copy = QRCode("qrcode_binary_copy.txt", "01/09/2022", "Xuanpu", 0.1)
        >>> my_qrcode.equals(my_qrcode_copy)
        True
        '''
        return self.data.equals(another_qrcode.data) and \
               self.error_correction == another_qrcode.error_correction

    def is_corrupted(self, precise_qrcode):
        '''
        (QRCode) -> bool
        Returns True if this QRCode object is corrupted compared to a precise QRCode object, based on the error correction capability.
        
        >>> my_qrcode = QRCode("qrcode_binary.txt", "01/09/2024", "Vivian", 0.1)
        >>> my_c_qrcode = QRCode("qrcode_binary_c.txt", "01/09/2000", "Vivian", 0.1)
        >>> my_c_qrcode.is_corrupted(my_qrcode)
        True
        '''
        return not self.data.approximately_equals(precise_qrcode.data, self.error_correction)