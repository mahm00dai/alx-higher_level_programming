#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # Use symmetric difference to get elements present in only one set
    return set_1 ^ set_2
