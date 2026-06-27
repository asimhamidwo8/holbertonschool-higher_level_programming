#!/usr/bin/python3
"""Module that defines the BaseGeometry class with validation."""


class BaseGeometry:
    """A base class for geometry with area and integer validation."""

    def area(self):
        """Raise an Exception because area is not implemented yet."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer.

        Args:
            name (str): the name used in error messages.
            value (int): the value to validate.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
