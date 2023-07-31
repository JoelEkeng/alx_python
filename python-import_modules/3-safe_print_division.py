#!/usr/bin/python3


#safe_print_division = __import__('3-safe_print_division').safe_print_division

def safe_print_division(a, b):
    a = 12
    b = 0

    while True:
        try:
            if b == 0:
                print ("Cannot be divided by Zero.")
                break
        except:
            result = a / b
        finally:
            result = a / b
            print("{:d} / {:d} = {}".format(a, b, result))
            break


safe_print_division(12, 0)