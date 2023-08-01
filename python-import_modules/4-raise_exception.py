#!/usr/bin/python3

def raise_exception():
    print ("Exception has been raised")


try:
    raise_exception()
except TypeError as te:
    print ("Exception raised")        