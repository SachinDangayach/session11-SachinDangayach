import pytest
import random
import string
import session10
import os
import inspect
import re
from functools import reduce
from functools import singledispatch
from numbers import Integral
from collections.abc import Sequence
from decimal import Decimal
import pandas as pd

README_CONTENT_CHECK_FOR = [ # not needed to check as these are not required to be named similar
    'stock_exchange_details',
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    """get file content"""
    readme = open("README.md", "r", encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session10)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session10, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


############################## session10 Validations#############################

# TODO: 1 Test the named tuple performance is better than dictionary
def test_compare_perforamce():
    """
    Test to check the performance of namedtuple is better than dictinary
    """
    # Create fake profiles library by named tuples
    faker_db = session10.create_fake_library_by_namedtuple(100)

    # Create fake profiles library through dictionary
    faker_db_dict = session10.create_fake_library_by_dict(100)

    ntup, dict = session10.compare_time(faker_db, faker_db_dict)

    assert ntup<dict, "Implementation is not correct"

# TODO: 2 Test the named tuple performance is better than dictionary
def test_doc_string():
    """
    Test to check the doc string exists
    """
    # Create fake profiles library by named tuples
    faker_db = session10.create_fake_library_by_namedtuple(10)

    assert len(faker_db.__doc__) > 0 , "Doc string is missing"

# TODO: 2 Test the stock exchange details like high should be greater than low etc.
def test_stock_exchange():
    """
    Test to check the stock exchange numbers are correct
    """
    # create fake company profiles and list
    stock_exchange = session10.create_stock_exchange(num_of_listed_comp = 100)

    # Stock market details
    day_open,day_high,day_low,day_close = session10.stock_exchange_details(stock_exchange)

    assert day_low<=day_high, "Implementation of Stock Exchange is not correct"
    assert day_close<=day_high, "Implementation of Stock Exchange is not correct"
