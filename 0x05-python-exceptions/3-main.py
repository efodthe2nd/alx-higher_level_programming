#!/usr/bin/python3
safe_print = __import__('3-safe_print_division').safe_print_division

a = 12
b = 2
result = safe_print(a, b)
print("{:d} / {:d} = {:2f}".format(a, b, result))
