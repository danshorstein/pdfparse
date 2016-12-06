parsable
=======================
This is a simple parser designed to help parse table-like data from PDF files.

You must open a PDF file, select all, copy and paste into a text file. 

Then you can use parsable to specify column names and regular expressions for each
column's data. The rows are determined based on the column regular espressions plus either
spaces, or a seperator passed in as a regular expression.

Example:
fileinput text contains 
"""Assets
Current assets:
Cash and cash equivalents $ 18,347 $ 16,976
Marketable securities 46,048 48,460
Total cash, cash equivalents, and marketable securities (including securities
loaned of $4,058 and $2,574) 64,395 65,436
"""

    import parsable
    filename = r'filelocation\filename.txt'
    col_info = [('Description', r'.*?'),
                ('CY', r'[\d\,]+'),
                ('PY', r'[\d\,]+')]
    seperator = r'[\s\$]+'
    parse_df = parsable.simpleparse(testfile, col_info, seperator)
    print(parse_df)
    
returns a dataframe:
                                          Description       CY       PY
0                           Cash and cash equivalents   18,347   16,976
1                               Marketable securities   46,048   48,460
2                        loaned of $4,058 and $2,574)   64,395   65,436


TO DO:
------

ignore_rows - takes a list of regular expressions or row numbers, and ignores rows that match.  

add a complex parser, allowing more than one row of data to be concatenated into one row
