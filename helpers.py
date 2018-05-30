#!/usr/bin/python3
""" helpers.py
"""
from math import fabs
from math import floor

def times_list(li, dt):
    return [x * dt for x in li]

def times_tup(li, dt):
    return tuple(x * dt for x in li)

def float_gcd(a, b):
    if a < b:
        return float_gcd(b, a)
    if fabs(b) < 0.0001:
        return a
    else:
        return float_gcd(b, a - floor(a / b) * b)

