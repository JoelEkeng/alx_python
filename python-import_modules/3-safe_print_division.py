#!/usr/bin/python3


def safe_print_division(a, b):
    try:
        if b == 0:
            print ("Cannot be divided by Zero.")
            break
    except ZeroDivisionError:
            return None
    finally:
        result = a / b
        print("Inside result: {}".format(result))
        print("{:d} / {:d} = {}".format(a, b, result))
        break
