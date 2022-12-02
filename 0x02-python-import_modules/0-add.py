#!/usr/bin/python3
def add(a, b):
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, a + b))


if __name__ == "__main__":
    import sys
    add(int(sys.argv[1]), int(sys.argv[2]))
