#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum = 0
    for num in argv[1::]:
        sum += int(num)
    print(sum)
