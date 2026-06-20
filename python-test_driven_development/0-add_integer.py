#!/usr/bin/python3
import math

def add_integer(a, b=98):
    """Adds two integers."""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if math.isnan(a) or math.isnan(b):
        raise TypeError("a must be an integer")

    a = int(a)
    b = int(b)

    return a + b
