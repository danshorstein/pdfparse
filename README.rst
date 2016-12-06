pdfparse
=======================
This is a simple parser designed to help parse table-like data from PDF files.

You must open a PDF file, select all, copy and paste into a text file. 

Then you can use parsable to specify column names and regular expressions for each
column's data. The rows are determined based on the column regular espressions plus either
spaces, or a seperator passed in as a regular expression.

install with pip install git+git://git@github.com/danshorstein/pdfparse

TO DO:
------

ignore_rows - takes a list of regular expressions or row numbers, and ignores rows that match.  

add a complex parser, allowing more than one row of data to be concatenated into one row
