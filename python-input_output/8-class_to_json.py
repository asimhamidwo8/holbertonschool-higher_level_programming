#!/usr/bin/python3
"""Module that defines a function to convert a class instance to a dict."""


def class_to_json(obj):
    """Return the dictionary description of obj for JSON serialization.

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: A dictionary of the object's attributes.
    """
    return obj.__dict__
