#!/usr/bin/python3
for i in range(99):
    if i < 10:
        print("{:d} = 0x{:d}".format(i, i))
    elif i > 9:
        print("{:d} = 0x{:x}".format(i, i))
