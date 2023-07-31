#!/usr/bin/python3


def safe_print_division(a, b):
    result = None
    try:
        result = a / b
        if b == 0:
            print ("Cannot be divided by Zero.")
            break
    except ZeroDivisionError:
            return None
    finally:
        print("Inside result: {}".format(result))

        print("{:d} / {:d} = {}".format(a, b, result))
