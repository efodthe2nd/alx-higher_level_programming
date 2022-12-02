#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total = 0
    if len(sys.argv) == 1:
        print("0")
    elif len(sys.argv) == 2:
        print("{}".format(sys.argv[1]))
    elif len(sys.argv) > 2:
        for i in range(1, len(sys.argv)):
            total = int(sys.argv[i]) + total
        print("{}".format(total))
