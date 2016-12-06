# -*- coding: utf-8 -*-

"""
parsable PDF and other semi-structured table parsing
~~~~~~~~~~~~~~~~~~~~~
Parsable is a table-oriented parser designed to extract data from PDF files in semi-
structured table format
Basic simpleparse usage:
   >>> import parsable
   >>> parse = parsable.simpleparse(...

#TODO - FINISH!!!!....

:copyright: (c) 2016 by Daniel Shorstein.
:license: MIT license, see LICENSE for more details.
"""

__title__ = 'parsable'
__version__ = '0.0.1'
__author__ = 'Daniel Shorstein'
__license__ = 'MIT License'
__copyright__ = 'Copyright 2016 Daniel Shorstein'

# from .file_io import read_text_file, save_to_csv
from .regex_stuff import check_row_regex, get_column_regex, groupit
from .api import simpleparse
