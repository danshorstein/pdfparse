# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import re
from more_itertools import peekable

big_dict = {}

def import_data(fileloc):
    # do some test to make sure it's text, correct encoding, etc
    fh = open(fileloc, 'r')
    datalist = []
    for line in fh:
        datalist.append(line.strip('\n'))
        
    return datalist

def parse_data(datalist, ignore_rows=[], columns=[]):

    for col in columns:
        big_dict[col.name] = []
    
    for row in datalist:
        for ignore in ignore_rows:
            if re.search(ignore, row):
                # print 'ignored ' + row
                continue
        
        if columns[-1]._status == 1: 
            # write new row if columns are good
            write_row(columns)
            reset_status(columns)
        
        columnspk = peekable(columns)
            
        while columnspk.peek(None): 
            # add content if needed; skip if column is complete
            try:
                column = next(columnspk)
            except:
                break
            
            if column._status == 1:   
                continue
            if re.search(col.data_marker, row):
                value = re.findall(col.data_marker, row)
                if col.multiple_vals:
                    if col._contents:
                        col._contents.append(value)
                    else:
                        col._contents = [value]
                else:
                    col._contents = value[0]
            
            try:
                next_marker = columnspk.peek().data_marker
            except:
                break

            if re.search(next_marker, row):
                column._status = 1
        

def write_row(columns):
    for col in columns:
        big_dict[col.name].append(col._contents)
            
def reset_status(columns):
    for col in columns:
        col._status = 0
        col._contents = None
            
class Column(object):
    """
    The Column object allows the user to specify details for each column 
    desired for import. It contains the meat of the parsing, and drives
    what data is pulled in.
    
    Note there are two markers we need. First is to indicate when one column
    data search has ended and the next begins. This is done through the
    
    Parameters
    ----------
    name : string, defaults to None
        column name, which will be the final column label, but is also used
        to track which column instance is which
    data_marker : string, defaults to None
        this is a regular expression, used to grab the matching data
        note if more than one element matches, it will take the first match
    multiple_vals : boolean, defaults to False
        if True, the column will create a list for the first value that matches
        and append to the list until the complete marker is hit
    column_complete_marker : string, defaults to None
        this is a regular expression, used to indicate when this column is
        complete. This only applies if multiple_vals is True. Column will 
        also stop being added to when the next column's marker hits
    optional : boolean, defaults to False
        indicates whether getting a value for this column is required or 
        optional. If required, the parse_data function will not continue
        to the next row until all non-optional columns are populated
        
    Returns
    -------
    A column object used to create a row of data. 
    
    Examples
    --------
    TODO - ADD EXAMPLES!!!!
    """
    
    def __init__(self, name=None, data_marker=None, multiple_vals=False,
                 column_complete_marker=None, optional=False):
        
        self.name = name
        self.data_marker = data_marker
        self.multiple_vals = multiple_vals
        self.column_complete_marker = column_complete_marker
        self.optional = optional
        self._status = 0
        self._contents = None
        
    def get_name(self):
        return self.name
        
    def get_status(self):
        return self._status
        
a = import_data(r'E:\Users\daniel\Documents\GitHub\samplefiles\file.txt')

ignore_rows = ['^Part 2', '^SUPPLEMENT', '^U.S. Standard', '^Account Transactions',
               '^Bulletin No']

columns = [Column('TC', '^(\D\d\d\d) To'),
           Column('Description', '^\D\d\d\d (To.*)', True, '^Comment'),
           Column('Comment', '^Comment', True, '^Reference', True),
           Column('Reference', '^Reference', True, '^Budgetary Entry', True),
           ]

b= parse_data(a, ignore_rows, columns)