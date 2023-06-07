#!/usr/bin/python3
def print_last_digit(num):
    '''prints the last digit of a number'''
    last_digit = abs(num) % 10
    print(f"{last_digit}", end='')
    return last_digit
