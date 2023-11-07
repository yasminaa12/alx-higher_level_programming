#!/usr/bin/python3
"""Reads from the standard input and computes metrics."""


def print_stats(size, status_codes):
    """Print accumulated metrics"""

    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    Count = 0

    try:
        for Line in sys.stdin:
            if Count == 10:
                print_stats(size, status_codes)
                Count = 1
            else:
                Count += 1

            Line = Line.split()

            try:
                size += int(Line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if Line[-2] in valid_codes:
                    if status_codes.get(Line[-2], -1) == -1:
                        status_codes[Line[-2]] = 1
                    else:
                        status_codes[Line[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
