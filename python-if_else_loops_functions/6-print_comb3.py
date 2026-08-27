#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i + 1, 10):
        for k in range(j + 1, 10):
            if i == 7 and j == 8 and k == 9:
                print("{}{}{}".format(i, j, k), end="")
            else:
                print("{}{}{}".format(i, j, k), end=", ")
