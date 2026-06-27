#!/usr/bin/python3
"""Module defining VerboseList, a list that announces its changes."""


class VerboseList(list):
    """A list subclass that prints a message on add/remove operations."""

    def append(self, item):
        """Append an item and announce it."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extend the list and announce how many items were added."""
        items = list(iterable)
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, item):
        """Announce then remove an item from the list."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Announce then pop the item at the given index (default last)."""
        print("Popped [{}] from the list.".format(self[index]))
        return super().pop(index)
