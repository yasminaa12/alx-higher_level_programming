#!/usr/bin/python3
for a in range(0, 8):
    for j in range(a + 1, 10):
        print("{}{}".format(a, j), end=', ')
print("{}{}".format(a + 1, j))
