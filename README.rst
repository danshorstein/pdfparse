parsicle
=======================
This is just another parser, designed to parse table-like data extracted as text from PDF files via copy/paste.
The desired output is a pandas dataframe.

This project aims to provide a simple but powerful way to convert an unstructured or semi-structured PDF file,
have the user copy and paste the text into a .txt file or clipboard, then import into the extractor. 

The user will have to provide columns as objects, each of which will have methods
that identify information about when/where/how to populate the records/rows for each column. 

The parser will also take an optional input of regular expressions to identify rows to delete, or the 
actual row numbers to delete. This is especially helpful if the text has repeating headers and footers. 
