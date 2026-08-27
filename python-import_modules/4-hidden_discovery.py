#!/usr/bin/python3

import subprocess

if __name__ == "__main__":
    result = subprocess.check_output(
        ["strings", "/tmp/hidden_4.pyc"], text=True
    )


    names = []

    for line in result.splitlines():
        if line.startswith("__"):
            continue
        if line.isidentifier():
            names.append(line)

    for name in sorted(set(names)):
        print(name)
