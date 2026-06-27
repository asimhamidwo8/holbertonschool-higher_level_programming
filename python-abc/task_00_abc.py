#!/usr/bin/python3
"""Module defining an abstract Animal class and its subclasses."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing a generic animal."""

    @abstractmethod
    def sound(self):
        """Return the sound the animal makes. Implemented by subclasses."""
        pass


class Dog(Animal):
    """A dog, a concrete Animal that barks."""

    def sound(self):
        """Return the dog's sound."""
        return "Bark"


class Cat(Animal):
    """A cat, a concrete Animal that meows."""

    def sound(self):
        """Return the cat's sound."""
        return "Meow"
