#!/usr/bin/python3
"""Module that defines MyList, a subclass of the built-in list."""


class MyList(list):
    """A list subclass that can print its elements sorted."""

    def print_sorted(self):
        """Print the list in ascending order without modifying it."""
        print(sorted(self))
