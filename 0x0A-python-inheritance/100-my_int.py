#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """Invert int operators == and !=."""

    def __eq__(self, val):
        """Override == opeartor with != behavior."""
        return self.real != val

    def __ne__(self, val):
        """Override != operator with == behavior."""
        return self.real == val
