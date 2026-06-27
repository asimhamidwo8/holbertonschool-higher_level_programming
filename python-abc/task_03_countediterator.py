#!/usr/bin/python3
"""Module defining CountedIterator, an iterator that counts its items."""


class CountedIterator:
    """Wrap an iterable and count how many items have been fetched."""

    def __init__(self, iterable):
        """Initialize the wrapped iterator and a zeroed counter.

        Args:
            iterable: any iterable to iterate over.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """Return the next item and increment the counter.

        Raises:
            StopIteration: when the underlying iterator is exhausted.
        """
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """Return how many items have been iterated so far."""
        return self.count
