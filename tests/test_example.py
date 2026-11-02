"""An example test, to be copied and then deleted.

Requirement 9 asks for two tests on your own classes. This file shows the two
shapes you need, using a throwaway class defined right here. Run it with:

    pytest

Neither of these tests counts toward requirement 9 — they do not touch your
system. Copy the shapes into a file of your own, point them at your classes,
and delete this file.
"""

import pytest


class Jar:
    """A throwaway class, here only so the examples have something to test."""

    def __init__(self):
        self._count = 0
        self.contents = []

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        if value < 0:
            raise ValueError("A count cannot be negative")
        self._count = value

    def add(self, item):
        if len(self.contents) >= 2:
            print("The jar is full.")
            return
        self.contents.append(item)


def test_setter_refuses_an_invalid_value():
    """Shape 1: prove the setter raises instead of storing."""
    jar = Jar()
    with pytest.raises(ValueError):
        jar.count = -1


def test_a_refusal_changes_nothing():
    """Shape 2: prove the collection is the same length after a refusal."""
    jar = Jar()
    jar.add("one")
    jar.add("two")
    before = len(jar.contents)

    jar.add("three")

    assert len(jar.contents) == before
