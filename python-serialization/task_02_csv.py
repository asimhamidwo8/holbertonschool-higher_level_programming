#!/usr/bin/env python3
"""Module for converting CSV data to JSON."""

import csv
import json


def convert_csv_to_json(filename):
    """Convert a CSV file to JSON and save it as data.json.

    Args:
        filename (str): The path to the CSV file.

    Returns:
        bool: True if conversion succeeds, False otherwise.
    """
    try:
        with open(filename, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except (FileNotFoundError, OSError):
        return False
