#!/usr/bin/python3

class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be an number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

    def __eq__(self, other):
        """Override the equality operator."""
        if isinstance(other, Square):
            return self.__size == other.__size
        return False

    def __ne__(self, other):
        """Override the inequality operator."""
        return not self.__eq__(other)

    def __lt__(self, other):
        """Override the less than operator."""
        if isinstance(other, Square):
            return self.__size < other.__size
        return NotImplemented

    def __le__(self, other):
        """Override the less than or equal to operator."""
        if isinstance(other, Square):
            return self.__size <= other.__size
        return NotImplemented

    def __gt__(self, other):
        """Override the greater than operator."""
        if isinstance(other, Square):
            return self.__size > other.__size
        return NotImplemented

    def __ge__(self, other):
        """Override the greater than or equal to operator."""
        if isinstance(other, Square):
            return self.__size >= other.__size
        return NotImplemented
