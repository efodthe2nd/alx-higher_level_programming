#!/usr/bin/python3
"""Dispalys the X-Request-Id of a url passed as argument"""

import urlib.request
import sys


def main():
    with urllib.request.urlopen(sys.argv[1]) as response:
        header = response.getheader("X-Request-Id")

    print(header)


if __name__ == '__main__':
    main()
