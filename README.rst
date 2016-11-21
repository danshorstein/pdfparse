parsable
=======================
This is just another parser, designed to parse table-like data extracted as text from PDF files via copy/paste.
The desired output is a pandas dataframe. I'm a CPA, and not a programmer, other than I've been playing around
with Python for the past couple years and figured out it is awesome, and I want it to do 90% of my work for me.
So here I am, trying to make it do my work for me, and at the same time help other people do their work for them too.

The way this works is the copied/pasted PDF text is imported into parsable, turned into a list of strings (like rows),
and then parsed based on the user's inputs. Many rows will need to be ignored or deleted.

I have not been able to find any parsers or PDF readers that are very helpful in doing what this 
is intended to do (I tried parsimonious, which is awesome, but doesn't quite work how I need it to), so here we are.

This project aims to provide a simple but powerful way to convert an unstructured or semi-structured PDF file,
have the user copy and paste the text into a .txt file or clipboard, then import into the extractor. 

The user will have to provide columns as objects, each of which will have methods
that identify information about when/where/how to populate the records/rows for each column. 

The parser will also take an optional input of regular expressions to identify rows to delete, or the 
actual row numbers to delete. This is especially helpful if the text has repeating headers and footers. 

-------
TO DO:

learn how to write python

Add dependencies (pandas, clipboard?, re)

Come up with class/method/functions. General thoughts are:
import_text - gets the data into python via clipboard or txt file. user must open PDF file, 
    select all, copy, then paste to txt or unload clipboard ***I would love to find a way to replace this
    with a pythonic method, but I can't find any solutions that provide text in exactly the same format
    as you get when you open PDF file, select all, copy, and paste***

ignore_rows - takes a list of regular expressions or row numbers, and ignores rows that match.  
    (Make sure it can handle both regex and number)

column - object that represents each column of information desired. has the following attributes/methods/whatever:
    .dtype - type of data in the column, can be str, int, float, list, date. defaults to str, unless all match another... 
        (maybe let pandas try and figure it out)
    .marker - regex expression (maybe allow a list?) to indicate what exactly is wanted from each "row" of information
    .optional - flag indicating whether the column is optional or not
    .order - indicates the order columns are populated. this is important in case of conflicting regular expressions
    .status - (0,1, or 2?) during the iteration of populating each row, indicates whether column in that row is
        unpopulated, inprocess, or complete
        
MORE TO COME
    
