#!/usr/bin/python3
"""Print names defined by hidden_4.pyc."""

import hidden_4


if __name__ == "__main__":
    for name in sorted(dir(hidden_4)):
        if not name.startswith("__"):
            print(name)