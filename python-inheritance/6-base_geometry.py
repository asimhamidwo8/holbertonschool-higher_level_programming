#!/usr/bin/python3
"""Module that defines the BaseGeometry class."""


class BaseGeometry:
    """A base class for geometry with an unimplemented area method."""

    def area(self):
        """Raise an Exception because area is not implemented yet."""
        raise Exception("area() is not implemented"
