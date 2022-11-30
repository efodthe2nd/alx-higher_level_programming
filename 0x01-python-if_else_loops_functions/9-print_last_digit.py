#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        new_number = number % 10
    elif number < 0:
        new_number = number % -10
        new_number = new_number * -1
    print("{:d}".format(new_number), end="")
    return new_number
