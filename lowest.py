# lowest.py
# A non-serious attempt at creating a lowestcase implementation for python
# strings
# Author: Paul Langton
import sys

lowest_rules = {
        ' ': ' ',
        'a': 'o',
        'b': 'o',
        'c': '_',
        'd': 'o',
        'e': 'o',
        'f': 'l',
        'g': 'o',
        'h': 'l',
        'i': ':',
        'j': ':',
        'k': 'l',
        'l': 'l',
        'm': '_',
        'n': '_',
        'o': 'o',
        'p': 'o',
        'q': 'o',
        'r': '_',
        's': '_',
        't': 'l',
        'u': '_',
        'v': '_',
        'w': '_',
        'x': '_',
        'y': 'l',
        'z': '_',
        }

def lowest(s):
    """
    returns s in lowest-case
    - all the letters with tall bits become l
    - all the letters with holes become o
    - all the dotted boyes become :
    - all the other ones get squashed to become _
    converts 
    """
    ls = ""
    s = s.lower()
    for c in s:
        if c in lowest_rules.keys():
            ls += lowest_rules[c]
        else:
            ls += c
    return ls


