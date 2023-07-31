#!/usr/bin/python3


safe_print_division = __import__('3-safe_print_division').safe_print_division

def safe_print_division(a, b):
    a = 12
    b = 0

    while True:
        try:
            result = a / b
            print("{:d} / {:d} = {}".format(a, b, result))
            break
        except ZeroDivisionError:
            print("{} cannot not be divided by zero".format(a)) 
            break
