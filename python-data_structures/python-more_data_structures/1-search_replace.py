#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Returns a new list with replaced elements"""
    return [replace if item == search else item for item in my_list]
