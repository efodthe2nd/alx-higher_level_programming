#!/usr/bin/python3
safe_print = __import__('2-safe_print_list_integers').safe_print_list_integers

my_list = [1, 2, "School", 3, 4 ,5, [1, 2, 3]]

nb_print = safe_print(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
