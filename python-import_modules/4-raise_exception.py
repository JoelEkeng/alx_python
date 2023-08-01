#!/usr/bin/python3

def raise_exception():
    return ("Exception has been raised")


try:
    raise_exception()
except TypeError as te:
    print ("Exception raised")        