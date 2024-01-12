#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    current_dir = a_dictionary.copy()
    list_key = list(current_dir.keys())
    for i in list_key:
        current_dir[i] *= 2
    return (current_dir)
