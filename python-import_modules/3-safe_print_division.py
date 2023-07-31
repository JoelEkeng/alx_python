#!/usr/bin/python3


def safe_print_division(a, b):
    while True:
        a = 10
        b = 2
        try:
            if b == 0:
                print ("Cannot be divided by Zero.")
                break
        except:
            result = a / b
        finally:
            result = a / b
            print("Inside result: {}".format(result))
            print("{:d} / {:d} = {}".format(a, b, result))
            break
