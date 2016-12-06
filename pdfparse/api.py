import re
import pandas as pd
from .file_io import read_text_file
from .regex_stuff import check_row_regex, get_column_regex, groupit

#TODO - delete below stuff once ok
# def simpleparse(filename, row_regex, col_list, col_regex, skiprow_regex=None):
#     """
#     A simple PDF file parser. This takes a txt file input,
#     and user defines the regular expressions to capture
#     the rows and columns to output. This method is ideal
#     if all of the rows from which we want to capture data
#     are in the same format, meaning we don't have any data
#     wrapping issues to capture (see complexparse for   #TODO - add complexparse!
#     data wrapping parsing)

#     :param filename: location of the text file to parse. This should a copied and
#             pasted PDF file.
#     :param row_regex: List of regular expressions to identify which rows should be
#             captured for purposes of building columns
#     :param col_list: List of column names as strings. The lenth of this list equal
#             match the lenth of col_regex
#     :param col_regex: List of regular expressions to identify which part of the
#             row data each column should be populated with
#     :param skiprow_regex: (optional) List of regular expressions to identify which rows
#             that would otherwise be captured in the row_ids should be excluded
#             from rows to capture columns
#     :return: pandas DataFrame object

#     """

#     data = read_text_file(filename)

#     columns = {col:[] for col in col_list}

#     column_capture = {coldata[0]:coldata[1] for coldata in zip(col_list, col_regex)}

#     for row in data:
#         if check_row_regex(row, row_regex):
#             for col in column_capture:
#                 columns[col].append(get_column_regex(row, column_capture[col]))

#     column_df = pd.DataFrame.from_dict(columns)

#     return column_df[col_list]

def simpleparse(filename, col_info, seperator=r'\s+', skiprow_regex=None):
    """
    A simple PDF file parser. This takes a txt file input,
    and user defines the regular expressions to capture
    the rows and columns to output. This method is ideal
    if all of the rows from which we want to capture data
    are in the same format, meaning we don't have any data
    wrapping issues to capture

    :param filename: location of the text file to parse. This should a copied and
            pasted PDF file.
    :param col_info: List of two-item tuples that contain column name and 
            regular expressions to identify the column spot. in simpleparse,
            these regular expressions are concatenated with a separator to create
            the row identifier, meaning the concatenated regex is used to identify which
            rows should be used to search for the underlying column data
    :param seperator: String regular expression used to indicate separation between
            the column data. May be just a space or more than one space
    :param skiprow_regex: (optional) List of regular expressions to identify which rows
            that would otherwise be captured in the row_ids should be excluded
            from rows to capture columns
    :return: pandas DataFrame object

    """
    #TODO - break some of these out into seperate functions...

    col_info = [(item[0], groupit(item[1])) for item in col_info]

    data = read_text_file(filename)

    row_regex_items = [regex[1] for regex in col_info]

    row_regex = re.compile((seperator).join(row_regex_items))

    col_list = [col[0] for col in col_info]

    columns = {col:[] for col in col_list}

    column_capture = {coldata[0]:(row_regex, numb) for (numb, coldata) in enumerate(col_info)}

    for row in data:
        if check_row_regex(row, row_regex):
            for col, data in column_capture.items():
                col_regex = data[0]
                group = data[1] + 1

                columns[col].append(get_column_regex(row, col_regex, group))

    column_df = pd.DataFrame.from_dict(columns)

    return column_df[col_list]
