#!/usr/bin/python3

def common_elements(set_1, set_2):
    # This checks for common elements in the set using the '&' 
    common_element = set(set_1 & set_2)

    return common_element
