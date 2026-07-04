#!/usr/bin/python3
"""Module that defines a function to load an object from a JSON file."""
import json


def load_from_json_file(filename):
    """Create an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to read from.

    Returns:
        object: The Python data structure represented by the file content.
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
