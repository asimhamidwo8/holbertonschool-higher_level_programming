#!/usr/bin/python3
"""Print names defined by hidden_4.pyc."""

import re


if __name__ == "__main__":
    with open("/tmp/hidden_4.pyc", "rb") as file:
        data = file.read()

    names = set(re.findall(
        rb"[A-Za-z_][A-Za-z0-9_]*",
        data
    ))

    for name in sorted(names):
        name = name.decode()
        if (
            not name.startswith("__")
            and name in {
                "my_secret_santa",
                "print_hidden",
                "print_school",
            }
        ):
            print(name)
