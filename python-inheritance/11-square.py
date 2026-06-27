#!/usr/bin/python3
"""Module that defines a Square with its own string representation."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square: a rectangle whose width and height are equal."""

    def __init__(self, size):
        """Initialize the square after validating its size.

        Args:
            size (int): the side length, must be a positive integer.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return the square description: [Square] <width>/<height>."""
        return "[Square] {}/{}".format(self.__size, self.__size)
