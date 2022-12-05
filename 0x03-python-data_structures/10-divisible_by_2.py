#!/usr/bin/python
def divisible_by_2(my_list=[]):
    new_list = [i*0 for i in range(len(my_list))]

    for i in range(len(my_list)):
        if i % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)

    return (new_list)
