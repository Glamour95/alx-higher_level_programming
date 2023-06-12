#!/usr/bin/python3
"""
This module defines the MyInt class that inherits from int.
"""

class MyInt(int):
    """
    Represents a custom integer class.
    """

    def __eq__(self, other):
        """
        Overrides the == operator.

        Args:
            other: The value to compare with.

        Returns:
            bool: True if not equal, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the != operator.

        Args:
            other: The value to compare with.

        Returns:
            bool: True if equal, False otherwise.
        """
        return super().__eq__(other)
