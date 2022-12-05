#!/usr/bin/python3
print_list_integer = __import__('0-print_list_integer').print_list_integer
replace_in_list = __import__('2-replace_in_list').replace_in_list
my_list = [1,2,4,5]
print_list_integer(my_list)
new_list = replace_in_list(my_list, 2, 5)
print(new_list)
