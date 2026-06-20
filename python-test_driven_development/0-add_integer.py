#!/usr/bin/python3
"""Adds two integers."""


def add_integer(a, b=98):
    """Return sum of two integers."""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # منع NaN و inf بدون import
    if a != a or b != b:
        raise TypeError("a must be an integer")

    if a in (float('inf'), float('-inf')) or b in (float('inf'), float('-inf')):
        raise TypeError("a must be an integer")

    return int(a) + int(b)
