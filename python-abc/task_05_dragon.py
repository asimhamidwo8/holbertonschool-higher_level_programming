#!/usr/bin/python3
"""Module demonstrating mixins with a Dragon class."""


class SwimMixin:
    """Mixin that grants the ability to swim."""

    def swim(self):
        """Print that the creature swims."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that grants the ability to fly."""

    def fly(self):
        """Print that the creature flies."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A dragon that can both swim and fly, and also roar."""

    def roar(self):
        """Print that the dragon roars."""
        print("The dragon roars!")
