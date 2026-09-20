#!/usr/bin/env python3
"""Print names defined in hidden_4.pyc."""

from xdis import load_module


def find_names(code):
    """Find names recursively in code objects."""
    names = set(code.co_names)

    for const in code.co_consts:
        if hasattr(const, "co_names"):
            names.update(find_names(const))

    return names


if __name__ == "__main__":
    result = load_module("/tmp/hidden_4.pyc")
    code = result[3]

    for name in sorted(find_names(code)):
        if not name.startswith("__"):
            print(name)
