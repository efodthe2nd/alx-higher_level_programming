#!/usr/bin/python3
for i in range(99):
    if i < 10:
        print("{} = 0x{}".format(i, i))
    elif i > 9:
        print("{} = 0x{:x}".format(i, i))
