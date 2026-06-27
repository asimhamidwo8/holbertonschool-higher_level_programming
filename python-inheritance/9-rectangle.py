#!/usr/bin/python3
"""Module that defines a Rectangle with area and string representation."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle defined by a validated width and height."""

    def __init__(self, width, height):
        """Initialize the rectangle after validating its dimensions.

        Args:
            width (int): the width, must be a positive integer.
            height (int): the height, must be a positive integer.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the rectangle description: [Rectangle] <width>/<height>."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
