#!/usr/bin/env python3

def no_c(my_string):
    words = ""

    for alphabets in my_string:
        if alphabets != "C" and alphabets != "c":
            words += alphabets
            
    return words
