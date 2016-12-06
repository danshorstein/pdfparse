# -*- coding: utf-8 -*-

"""
parsable.regex_stuff
~~~~~~~~~~~~~~~
This module provides functions to check the rows and columns 
for regular expressions passed to them
"""

#TODO - build a column regex maker using groupit and row regex. see test2 from testing!

def check_row_regex(row, row_regex):
    '''grabs rows using regex'''
    if row_regex.match(row):
        return row


def get_column_regex(row, col_regex, group=1):
    '''gets matches for col in row'''
    try:
        return col_regex.match(row).group(group)
    except:
        print('could not do shit with {}, {}'.format(row, col_regex))


def groupit(regex):
    '''groups the regex passed in'''
    return '(' + regex + ')'
