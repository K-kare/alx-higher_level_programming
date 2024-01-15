#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
        final_digit = number % 10
        print("{}".format(final_digit), end='')
        return (final_digit)
