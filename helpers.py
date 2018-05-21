#!/usr/bin/python3
""" helpers.py
"""

def times_list(li, dt):
    return [x * dt for x in li]

def times_tup(li, dt):
    return tuple(x * dt for x in li)
