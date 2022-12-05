#!/usr/bin/python3

def no_c(my_string):
    strm = ''
    for j in my_string:
        if j != 'c' and j != 'C':
            strm += j
        return (strm)
